"""add content column to posts table

Revision ID: e70c42fd5cc4
Revises: 81df5002d5ee
Create Date: 2022-05-09 19:18:45.312530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70c42fd5cc4'
down_revision = '81df5002d5ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
