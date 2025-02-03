"""hola18

Revision ID: 25961810a427
Revises: fefff2eb517d
Create Date: 2025-02-02 15:26:05.321543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25961810a427'
down_revision: Union[str, None] = 'fefff2eb517d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('teacher_request_mean_teacher_id_fkey', 'teacher_request_mean', type_='foreignkey')
    op.drop_constraint('teacher_request_mean_mean_id_fkey', 'teacher_request_mean', type_='foreignkey')
    op.create_foreign_key(None, 'teacher_request_mean', 'teacher', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'teacher_request_mean', 'mean', ['mean_id'], ['entity_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher_request_mean', type_='foreignkey')
    op.drop_constraint(None, 'teacher_request_mean', type_='foreignkey')
    op.create_foreign_key('teacher_request_mean_mean_id_fkey', 'teacher_request_mean', 'mean', ['mean_id'], ['entity_id'])
    op.create_foreign_key('teacher_request_mean_teacher_id_fkey', 'teacher_request_mean', 'teacher', ['teacher_id'], ['id'])
    # ### end Alembic commands ###
