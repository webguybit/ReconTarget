"""empty message

Revision ID: 1fa351a62074
Revises: 36f00eeb68fa
Create Date: 2020-06-11 12:44:09.638418

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1fa351a62074'
down_revision = '36f00eeb68fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_target', sa.Column('target_status_cod', sa.String(length=4), nullable=True))
    op.drop_column('tb_target', 'target_status_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_target', sa.Column('target_status_code', mysql.VARCHAR(length=3), nullable=True))
    op.drop_column('tb_target', 'target_status_cod')
    # ### end Alembic commands ###
