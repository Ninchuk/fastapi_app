"""add rewiew

Revision ID: 496aad61dcef
Revises: 70f9acc1d3b4
Create Date: 2024-01-15 07:14:55.165341

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "496aad61dcef"
down_revision: Union[str, None] = "70f9acc1d3b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "review",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("body", mysql.TEXT(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.alter_column(
        "product",
        "description",
        existing_type=sa.VARCHAR(),
        type_=mysql.TEXT(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "product",
        "description",
        existing_type=mysql.TEXT(),
        type_=sa.VARCHAR(),
        nullable=False,
    )
    op.drop_table("review")
    # ### end Alembic commands ###