"""init_user

Revision ID: ac2605b618bb
Revises: 
Create Date: 2022-08-09 04:11:31.558251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac2605b618bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=255), nullable=False),
    sa.Column('edited_date', sa.DateTime(), nullable=True),
    sa.Column('edited_by', sa.String(length=255), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='user_email_unique'),
    sa.UniqueConstraint('username', name='user_username_unique')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###