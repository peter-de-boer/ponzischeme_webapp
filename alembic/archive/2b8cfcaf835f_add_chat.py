"""add chat

Revision ID: 2b8cfcaf835f
Revises: f7d61a1e1cb4
Create Date: 2019-03-04 20:05:16.672673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b8cfcaf835f'
down_revision = None
#down_revision = 'f7d61a1e1cb4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('games', sa.Column('chat', sa.PickleType))


def downgrade():
    op.drop_column('games', 'chat')
