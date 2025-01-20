"""tns_auto_report_allow_bots

Revision ID: 94c30396a122
Revises: a4fd59613f77
Create Date: 2024-05-28 15:48:28.174518

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "94c30396a122"
down_revision = "a4fd59613f77"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tnsrobot_groups",
        sa.Column(
            "auto_report_allow_bots",
            sa.Boolean(),
            nullable=False,
            server_default="false",
        ),
    )
    op.add_column(
        "tnsrobot_submissions",
        sa.Column("custom_remarks_string", sa.String(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tnsrobot_submissions", "custom_remarks_string")
    op.drop_column("tnsrobot_groups", "auto_report_allow_bots")
    # ### end Alembic commands ###
