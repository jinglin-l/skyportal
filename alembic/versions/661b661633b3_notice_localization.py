"""notice_localization

Revision ID: 661b661633b3
Revises: 0943fbb6faf0
Create Date: 2023-03-22 18:14:09.788610

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "661b661633b3"
down_revision = "0943fbb6faf0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "gcnnotices",
        sa.Column(
            "has_localization", sa.Boolean(), server_default="true", nullable=False
        ),
    )
    op.add_column(
        "gcnnotices",
        sa.Column(
            "localization_ingested",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
    )
    op.add_column("localizations", sa.Column("notice_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, "localizations", "gcnnotices", ["notice_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "localizations", type_="foreignkey")
    op.drop_column("localizations", "notice_id")
    op.drop_column("gcnnotices", "localization_ingested")
    op.drop_column("gcnnotices", "has_localization")
    # ### end Alembic commands ###
