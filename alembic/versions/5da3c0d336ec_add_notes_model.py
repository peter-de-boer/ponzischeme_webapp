"""add Notes model

Revision ID: 5da3c0d336ec
Revises: 
Create Date: 2019-04-07 15:25:39.748089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5da3c0d336ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'notes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('notes', sa.String),
        sa.Column('player_id', sa.Integer,  sa.ForeignKey('users.id')),
        sa.Column('game_id', sa.Integer,  sa.ForeignKey('games.id'))

    )


def downgrade():
    pass
