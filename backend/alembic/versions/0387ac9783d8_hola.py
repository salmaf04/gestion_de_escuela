"""hola

Revision ID: 0387ac9783d8
Revises: 0769a22dbce8
Create Date: 2025-02-02 12:27:47.594918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0387ac9783d8'
down_revision: Union[str, None] = '0769a22dbce8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('teacher_id_fkey', 'teacher', type_='foreignkey')
    op.create_foreign_key(None, 'teacher', 'user', ['id'], ['entity_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.create_foreign_key('teacher_id_fkey', 'teacher', 'user', ['id'], ['entity_id'])
    # ### end Alembic commands ###
