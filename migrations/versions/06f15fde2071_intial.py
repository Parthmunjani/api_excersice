"""intial

Revision ID: 06f15fde2071
Revises: df4a3473a9ea
Create Date: 2023-05-08 12:15:37.758246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06f15fde2071'
down_revision = 'df4a3473a9ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_price', sa.Float(), nullable=True))
        batch_op.alter_column('payment_status',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_order', schema=None) as batch_op:
        batch_op.alter_column('payment_status',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.drop_column('total_price')

    # ### end Alembic commands ###
