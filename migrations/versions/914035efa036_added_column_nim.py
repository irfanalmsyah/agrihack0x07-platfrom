"""added_column_nim

Revision ID: 914035efa036
Revises: 5f301afbcc20
Create Date: 2022-10-16 22:07:17.265796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '914035efa036'
down_revision = '5f301afbcc20'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("nim", sa.String(11)))


def downgrade():
    pass
