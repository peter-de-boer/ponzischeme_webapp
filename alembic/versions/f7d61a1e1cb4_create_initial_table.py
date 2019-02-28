"""create initial table

Revision ID: f7d61a1e1cb4
Revises: 
Create Date: 2019-02-28 19:15:39.241732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d61a1e1cb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('confirmed', sa.Boolean))


def downgrade():
    sa.drop_column('users', 'confirmed')
