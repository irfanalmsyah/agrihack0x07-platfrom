"""add ispeserta column

Revision ID: 9463a4264742
Revises: 914035efa036
Create Date: 2022-10-17 19:15:37.488898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9463a4264742'
down_revision = '914035efa036'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('ispeserta', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'ispeserta')
    # ### end Alembic commands ###