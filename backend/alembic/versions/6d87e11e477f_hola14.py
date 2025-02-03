"""hola14

Revision ID: 6d87e11e477f
Revises: 187e34cefc09
Create Date: 2025-02-02 14:53:15.050077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d87e11e477f'
down_revision: Union[str, None] = '187e34cefc09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher_note', 'student_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.drop_constraint('teacher_note_student_id_fkey', 'teacher_note', type_='foreignkey')
    op.create_foreign_key(None, 'teacher_note', 'student', ['student_id'], ['id'], ondelete='SET NULL')
    op.drop_column('teacher_note', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher_note', sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'teacher_note', type_='foreignkey')
    op.create_foreign_key('teacher_note_student_id_fkey', 'teacher_note', 'student', ['student_id'], ['id'])
    op.alter_column('teacher_note', 'student_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###
