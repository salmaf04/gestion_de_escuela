"""hola3

Revision ID: 125c3bbc4cb2
Revises: 58060cf6c362
Create Date: 2025-02-02 12:46:55.588057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '125c3bbc4cb2'
down_revision: Union[str, None] = '58060cf6c362'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('dean_id_fkey', 'dean', type_='foreignkey')
    op.create_foreign_key(None, 'dean', 'teacher', ['id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dean', type_='foreignkey')
    op.create_foreign_key('dean_id_fkey', 'dean', 'teacher', ['id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
