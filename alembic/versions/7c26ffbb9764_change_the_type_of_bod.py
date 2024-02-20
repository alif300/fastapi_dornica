"""change the type of BoD

Revision ID: 7c26ffbb9764
Revises: b448c658bb96
Create Date: 2024-02-19 08:59:07.697143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c26ffbb9764'
down_revision: Union[str, None] = 'b448c658bb96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'DoB',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'DoB',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    # ### end Alembic commands ###