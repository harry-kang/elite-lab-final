"""Added hashkey and name to Chat tablele

Revision ID: 631aa3f93407
Revises: 35a7f096d5a0
Create Date: 2021-07-28 19:53:24.327213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '631aa3f93407'
down_revision = '35a7f096d5a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('chat', sa.Column('hash_key', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_chat_hash_key'), 'chat', ['hash_key'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chat_hash_key'), table_name='chat')
    op.drop_column('chat', 'hash_key')
    op.drop_column('chat', 'name')
    # ### end Alembic commands ###
