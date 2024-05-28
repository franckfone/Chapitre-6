"""empty message

Revision ID: 7a105bfc0cd0
Revises: cf1e8c1bc737
Create Date: 2021-09-20 18:41:43.017908

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a105bfc0cd0'
down_revision = 'cf1e8c1bc737'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('custom_domain', 'auto_create_regex')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('custom_domain', sa.Column('auto_create_regex', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    # ### end Alembic commands ###