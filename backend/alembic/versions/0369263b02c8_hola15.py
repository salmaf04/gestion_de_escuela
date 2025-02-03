"""hola15

Revision ID: 0369263b02c8
Revises: 6d87e11e477f
Create Date: 2025-02-02 15:11:49.060396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0369263b02c8'
down_revision: Union[str, None] = '6d87e11e477f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('student_id_fkey', 'student', type_='foreignkey')
    op.create_foreign_key(None, 'student', 'user', ['id'], ['entity_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_foreign_key('student_id_fkey', 'student', 'user', ['id'], ['entity_id'], ondelete='CASCADE')
    # ### end Alembic commands ###
