from sqlalchemy import and_
from sqlalchemy import event, select, func, inspect, update
from sqlalchemy.orm.attributes import get_history
from datetime import datetime, timedelta, timezone
from .tables import BaseTable, TeacherNoteTable, TeacherTable, StudentTable, StudentNoteTable, ValorationPeriodTable ,Roles, MeanMaintenanceTable, UserTable, AdministratorTable, SecretaryTable, DeanTable, MeanTable
import uuid

@event.listens_for(TeacherNoteTable, 'after_insert')
def update_teacher_average(mapper, connection, target):
    # Actualizar el promedio de valoraciones del profesor
    connection.execute(
        TeacherTable.__table__.update().
        where(TeacherTable.id == target.teacher_id).
        values(average_valoration=(
            select((func.sum(TeacherNoteTable.grade)/func.count())).
            where(TeacherNoteTable.teacher_id == target.teacher_id)
        ))
    )

def update_student_average(mapper, connection, target):
    # Actualizar el promedio de valoraciones del estudiante
    connection.execute(
        StudentTable.__table__.update().
        where(StudentTable.id == target.student_id).
        values(average_note=(
            select((func.sum(StudentNoteTable.note_value)/func.count())).
            where(StudentNoteTable.student_id == target.student_id)
        ))
    )

event.listen(StudentNoteTable, 'after_insert', update_student_average)
event.listen(StudentNoteTable, 'after_update', update_student_average)

@event.listens_for(BaseTable.metadata, 'after_create')
def insert_default_valoration_period(target, connection, **kw):
    # Verificar si la tabla creada es ValorationPeriodTable
    for table in target.tables.values():
        if table.name == ValorationPeriodTable.__tablename__:  
            # Comprobar si la tabla está vacía
            result = connection.execute(select(ValorationPeriodTable.entity_id)).fetchone()
            
            if result is None:
                # Insertar el periodo de valoración por defecto si la tabla está vacía
                connection.execute(
                    ValorationPeriodTable.__table__.insert().
                    values(
                        entity_id=uuid.uuid4(),
                        open=False
                    )
                )
            break
 
@event.listens_for(ValorationPeriodTable, 'after_update', propagate=True)
def update_less_than_three_valoration(mapper, connection, target):
    history = get_history(target, 'open')
    unchanged = history.unchanged[0] if history.unchanged else None
    old_value = history.deleted[0] if history.deleted else None
    new_value = history.added[0] if history.added else None


    if not unchanged :
        if old_value == True and new_value == False :
    # Actualizar el promedio de valoraciones del profesor
            connection.execute(
                TeacherTable.__table__.update().
                where(TeacherTable.average_valoration < 3).
                values(less_than_three_valoration= TeacherTable.less_than_three_valoration + 1)
                )
            
def insert_user_roles(mapper, connection, target):
    if target.type == "administrator" :
        target.roles = [Roles.ADMIN.value]
    elif target.type == "secretary" :
        target.roles = [Roles.SECRETARY.value]
    elif target.type == "teacher" :
        target.roles = [Roles.TEACHER.value]
    elif target.type == "student" :
        target.roles = [Roles.STUDENT.value]

for table in [TeacherTable, UserTable, AdministratorTable, SecretaryTable, StudentTable] :
    event.listen(table, 'before_insert', insert_user_roles)


@event.listens_for(DeanTable, 'before_insert')
def no_administrator(mapper, connection, target):
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    if result is None :
        target.roles = [Roles.DEAN.value, Roles.TEACHER.value, Roles.ADMIN.value]
    else :
        target.roles = [Roles.DEAN.value, Roles.TEACHER.value]

@event.listens_for(AdministratorTable, 'after_delete')
def check_administrator_after_delete(mapper, connection, target):
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    decano = connection.execute(select(DeanTable)).fetchone()
    if result is None :
        connection.execute(UserTable.__table__.update().values(roles=[Roles.DEAN.value, Roles.TEACHER.value, Roles.ADMIN.value]).where(UserTable.entity_id == decano.id))

@event.listens_for(AdministratorTable, 'before_insert')
def check_administrator_after_insert(mapper, connection, target):
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    decano = connection.execute(select(DeanTable)).fetchone()
    if result is None :
        connection.execute(UserTable.__table__.update().values(roles=[Roles.DEAN.value, Roles.TEACHER.value]).where(UserTable.entity_id == decano.id))


@event.listens_for(MeanMaintenanceTable, 'before_insert')
def check_replacement(mapper, connection, target):
    date = datetime.now(timezone.utc) - timedelta(days=365)
    result = connection.execute(
        select(
            func.count(MeanMaintenanceTable.entity_id).label("count")
        ).where(
            and_(
                MeanMaintenanceTable.date >= date,
                MeanMaintenanceTable.mean_id == target.mean_id
            )
        )
    ).scalars().first()

    if result >= 2 : 
        connection.execute(update(MeanTable).where(MeanTable.entity_id == target.mean_id).values(to_be_replaced=True))
    