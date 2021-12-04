"""add content column

Revision ID: ca47a8407f73
Revises: cb9451ed21d6
Create Date: 2021-12-03 19:29:23.606029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca47a8407f73'
down_revision = 'cb9451ed21d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
