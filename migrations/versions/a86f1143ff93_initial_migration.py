"""Initial migration.

Revision ID: a86f1143ff93
Revises: 2d2c123c7993
Create Date: 2023-07-20 15:41:23.296773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a86f1143ff93'
down_revision = '2d2c123c7993'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_permissions', schema=None) as batch_op:
        batch_op.drop_constraint('api_permissions_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_permissions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('api_permissions_user_id_fkey', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
