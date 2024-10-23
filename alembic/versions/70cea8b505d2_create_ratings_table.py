"""create ratings table

Revision ID: 70cea8b505d2
Revises: b75c070cefdd
Create Date: 2024-10-22 16:30:02.853159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70cea8b505d2'
down_revision: Union[str, None] = 'b75c070cefdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ratings',
        sa.Column('joke_id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('rating', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_table('ratings')
    pass
