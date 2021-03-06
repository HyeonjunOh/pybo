"""empty message

Revision ID: 9edd91922192
Revises: e9ffa07ce2e0
Create Date: 2020-10-14 21:12:23.401225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9edd91922192'
down_revision = 'e9ffa07ce2e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
