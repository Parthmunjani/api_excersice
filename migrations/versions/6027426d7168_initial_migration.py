"""Initial migration.

Revision ID: 6027426d7168
Revises: db4825e221f5
Create Date: 2023-07-19 10:31:37.077139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6027426d7168'
down_revision = 'db4825e221f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_roles',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='users_roles_role_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='users_roles_user_id_fkey')
    )
    # ### end Alembic commands ###
