"""hola10

Revision ID: b90f5688685d
Revises: 7d2d8c798700
Create Date: 2025-02-02 14:43:32.265199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b90f5688685d'
down_revision: Union[str, None] = '7d2d8c798700'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('mean_classroom_id_fkey', 'mean', type_='foreignkey')
    op.create_foreign_key(None, 'mean', 'classroom', ['classroom_id'], ['entity_id'], ondelete='SET NULL')
    op.drop_constraint('subject_course_id_fkey', 'subject', type_='foreignkey')
    op.create_foreign_key(None, 'subject', 'course', ['course_id'], ['entity_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subject', type_='foreignkey')
    op.create_foreign_key('subject_course_id_fkey', 'subject', 'course', ['course_id'], ['entity_id'], ondelete='SET NULL')
    op.drop_constraint(None, 'mean', type_='foreignkey')
    op.create_foreign_key('mean_classroom_id_fkey', 'mean', 'classroom', ['classroom_id'], ['entity_id'])
    # ### end Alembic commands ###
