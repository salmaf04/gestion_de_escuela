"""hola21

Revision ID: 645850074eb1
Revises: eea7e2899ba2
Create Date: 2025-02-02 19:50:51.265347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '645850074eb1'
down_revision: Union[str, None] = 'eea7e2899ba2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('secretary_id_fkey', 'secretary', type_='foreignkey')
    op.create_foreign_key(None, 'secretary', 'user', ['id'], ['entity_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'secretary', type_='foreignkey')
    op.create_foreign_key('secretary_id_fkey', 'secretary', 'user', ['id'], ['entity_id'], ondelete='CASCADE')
    # ### end Alembic commands ###
