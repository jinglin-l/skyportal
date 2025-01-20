"""Reference image migration

Revision ID: 999d3be6482f
Revises: 77788b2b56b2
Create Date: 2023-05-19 14:13:58.450844

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "999d3be6482f"
down_revision = "77788b2b56b2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "instrumentfields",
        sa.Column(
            "reference_filters",
            sa.ARRAY(sa.String()),
            nullable=True,
            comment="Reference template filters",
        ),
    )
    op.add_column(
        "instrumentfields",
        sa.Column(
            "reference_filter_mags",
            sa.ARRAY(sa.Float()),
            nullable=True,
            comment="Reference filter limiting magnitudes",
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("instrumentfields", "reference_filter_mags")
    op.drop_column("instrumentfields", "reference_filters")
    # ### end Alembic commands ###
