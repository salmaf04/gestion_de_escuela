"""hola9

Revision ID: 7d2d8c798700
Revises: cae0f6e61e00
Create Date: 2025-02-02 14:42:42.383097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d2d8c798700'
down_revision: Union[str, None] = 'cae0f6e61e00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('student_id_fkey', 'student', type_='foreignkey')
    op.create_foreign_key(None, 'student', 'user', ['id'], ['entity_id'], ondelete='CASCADE')
    op.drop_constraint('subject_classroom_id_fkey', 'subject', type_='foreignkey')
    op.drop_constraint('subject_course_id_fkey', 'subject', type_='foreignkey')
    op.create_foreign_key(None, 'subject', 'classroom', ['classroom_id'], ['entity_id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'subject', 'course', ['course_id'], ['entity_id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subject', type_='foreignkey')
    op.drop_constraint(None, 'subject', type_='foreignkey')
    op.create_foreign_key('subject_course_id_fkey', 'subject', 'course', ['course_id'], ['entity_id'])
    op.create_foreign_key('subject_classroom_id_fkey', 'subject', 'classroom', ['classroom_id'], ['entity_id'])
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_foreign_key('student_id_fkey', 'student', 'user', ['id'], ['entity_id'])
    # ### end Alembic commands ###
