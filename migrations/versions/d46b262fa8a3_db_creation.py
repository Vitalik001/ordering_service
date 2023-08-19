"""DB creation

Revision ID: d46b262fa8a3
Revises: 
Create Date: 2023-08-19 14:47:47.895683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd46b262fa8a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('total', sa.DECIMAL(), nullable=True),
    sa.Column('items', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stats',
    sa.Column('total_orders', sa.Integer(), nullable=True),
    sa.Column('total_order_price', sa.DECIMAL(), nullable=True),
    sa.Column('avg_order_price', sa.DECIMAL(), nullable=True),
    sa.Column('total_items', sa.Integer(), nullable=True),
    sa.Column('avg_items', sa.DECIMAL(), nullable=True),
    sa.Column('most_ordered_item', sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    op.drop_table('orders')
    op.drop_table('items')
    # ### end Alembic commands ###
