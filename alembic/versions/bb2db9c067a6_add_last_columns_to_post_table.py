"""add last columns to post table

Revision ID: bb2db9c067a6
Revises: e8b8ccd7e512
Create Date: 2021-12-03 19:50:17.183065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb2db9c067a6'
down_revision = 'e8b8ccd7e512'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable= False, server_default= 'TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
    pass
