"""empty message

Revision ID: e505cb517589
Revises: 83f4dbe125c4
Create Date: 2019-11-28 21:59:13.064634

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e505cb517589'
down_revision = '83f4dbe125c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_key',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('last_used', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('times', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('alias_used_on',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('gen_email_id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['gen_email_id'], ['gen_email.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gen_email_id', 'hostname', name='uq_alias_used')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alias_used_on')
    op.drop_table('api_key')
    # ### end Alembic commands ###
