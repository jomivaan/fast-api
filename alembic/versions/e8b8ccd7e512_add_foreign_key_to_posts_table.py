"""add foreign key to posts table

Revision ID: e8b8ccd7e512
Revises: 698548198afe
Create Date: 2021-12-03 19:41:19.465888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8b8ccd7e512'
down_revision = '698548198afe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table = "posts", referent_table = "users", local_cols=['owner_id'], remote_cols=['id'], ondelete= "CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk',table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
