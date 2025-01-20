"""Earthquake country migration

Revision ID: f870b311df53
Revises: 61f6f65746da
Create Date: 2022-11-20 21:29:00.420254

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f870b311df53"
down_revision = "61f6f65746da"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "earthquakenotices",
        sa.Column("country", sa.String(), nullable=True, comment="Country"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("earthquakenotices", "country")
    # ### end Alembic commands ###
