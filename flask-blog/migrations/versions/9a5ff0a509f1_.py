"""empty message

Revision ID: 9a5ff0a509f1
Revises: c6ed4ed1c565
Create Date: 2018-06-06 19:53:52.737407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5ff0a509f1'
down_revision = 'c6ed4ed1c565'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collections',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collections')
    # ### end Alembic commands ###