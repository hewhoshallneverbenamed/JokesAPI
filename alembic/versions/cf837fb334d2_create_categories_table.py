"""create categories table

Revision ID: cf837fb334d2
Revises: 867e34d379cb
Create Date: 2024-10-22 16:29:43.096666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf837fb334d2'
down_revision: Union[str, None] = '867e34d379cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('category_name', sa.String),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_table('categories')
    pass
