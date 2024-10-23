"""create jokes table

Revision ID: 867e34d379cb
Revises: 
Create Date: 2024-10-22 16:22:24.360060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '867e34d379cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'jokes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('joke_text', sa.String),
        sa.Column('category_id', sa.Integer),
        sa.Column('avg_rating', sa.Integer),
        sa.Column('num_ratings', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_table('jokes')
    pass
