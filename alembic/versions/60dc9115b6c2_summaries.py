"""Updates to allow for (AI) summaries on objs

Revision ID: 60dc9115b6c2
Revises: e268e17ca352
Create Date: 2023-03-05 23:24:29.121460

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "60dc9115b6c2"
down_revision = "e268e17ca352"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "analysis_services",
        sa.Column("display_on_resource_dropdown", sa.Boolean(), nullable=True),
    )
    op.add_column(
        "analysis_services", sa.Column("is_summary", sa.Boolean(), nullable=True)
    )
    op.add_column("objs", sa.Column("summary", sa.String(), nullable=True))
    op.add_column(
        "objs",
        sa.Column(
            "summary_history", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("objs", "summary_history")
    op.drop_column("objs", "summary")
    op.drop_column("analysis_services", "is_summary")
    op.drop_column("analysis_services", "display_on_resource_dropdown")
    # ### end Alembic commands ###
