"""empty message

Revision ID: 30656d5cdc95
Revises: 9f43635fe09b
Create Date: 2017-08-23 12:04:20.773907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30656d5cdc95'
down_revision = '9f43635fe09b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucket', sa.Column('modified_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucket', 'modified_at')
    # ### end Alembic commands ###