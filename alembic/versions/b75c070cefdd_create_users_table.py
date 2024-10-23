"""create users table

Revision ID: b75c070cefdd
Revises: cf837fb334d2
Create Date: 2024-10-22 16:29:55.956547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b75c070cefdd'
down_revision: Union[str, None] = 'cf837fb334d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
