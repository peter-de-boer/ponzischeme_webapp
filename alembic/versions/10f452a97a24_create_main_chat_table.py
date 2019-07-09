"""create main chat table

Revision ID: 10f452a97a24
Revises: 
Create Date: 2019-07-08 21:19:30.152879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f452a97a24'
down_revision = '5da3c0d336ec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'mainchat',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('chat', sa.PickleType)
    )


def downgrade():
    pass
