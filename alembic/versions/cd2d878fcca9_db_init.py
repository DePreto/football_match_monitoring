"""db_init

Revision ID: cd2d878fcca9
Revises: 
Create Date: 2022-12-25 09:49:33.757903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd2d878fcca9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('next_matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('datetime', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('next_matches')
    # ### end Alembic commands ###