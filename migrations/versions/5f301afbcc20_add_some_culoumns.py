"""add some culoumns

Revision ID: 5f301afbcc20
Revises: 4d3c1b59d011
Create Date: 2022-10-10 21:43:02.240989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f301afbcc20'
down_revision = '4d3c1b59d011'
branch_labels = None
depends_on = None
 

def upgrade():
    op.add_column("users", sa.Column("nama_lengkap", sa.String(128)))
    op.add_column("users", sa.Column("angkatan", sa.String(2)))

def downgrade():
    pass
