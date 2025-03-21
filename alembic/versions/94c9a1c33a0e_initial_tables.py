"""Initial tables

Revision ID: 94c9a1c33a0e
Revises: 
Create Date: 2025-02-10 21:14:25.139582

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '94c9a1c33a0e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('categories')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('categories_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categories_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=400), autoincrement=False, nullable=True),
    sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='products_category_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    # ### end Alembic commands ###
