"""create posts table

Revision ID: 81df5002d5ee
Revises: 
Create Date: 2022-05-09 18:39:41.585103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81df5002d5ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
