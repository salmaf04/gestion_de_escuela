"""Add less_than_3_valoration column to TeacherTable

Revision ID: ca82d6f13302
Revises: d17fff26596e
Create Date: 2025-01-31 23:03:45.887430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca82d6f13302'
down_revision: Union[str, None] = 'd17fff26596e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('less_than_three_valoration', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teacher', 'less_than_three_valoration')
    # ### end Alembic commands ###
