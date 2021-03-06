"""empty message

Revision ID: 043773cb30e2
Revises: 601d1095e267
Create Date: 2021-07-17 23:39:42.271745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043773cb30e2'
down_revision = '601d1095e267'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    # ### end Alembic commands ###
