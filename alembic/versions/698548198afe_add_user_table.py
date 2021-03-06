"""add user table

Revision ID: 698548198afe
Revises: ca47a8407f73
Create Date: 2021-12-03 19:34:41.074978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698548198afe'
down_revision = 'ca47a8407f73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email',sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
