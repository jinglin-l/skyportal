"""Request watchers migration

Revision ID: 2064509f3e08
Revises: f3647e87b69f
Create Date: 2022-12-27 22:56:54.827254

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "2064509f3e08"
down_revision = "f3647e87b69f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followup_request_users",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("followuprequest_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["followuprequest_id"], ["followuprequests.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "followup_request_users_forward_ind",
        "followup_request_users",
        ["followuprequest_id", "user_id"],
        unique=True,
    )
    op.create_index(
        "followup_request_users_reverse_ind",
        "followup_request_users",
        ["user_id", "followuprequest_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_followup_request_users_created_at"),
        "followup_request_users",
        ["created_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_followup_request_users_created_at"),
        table_name="followup_request_users",
    )
    op.drop_index(
        "followup_request_users_reverse_ind", table_name="followup_request_users"
    )
    op.drop_index(
        "followup_request_users_forward_ind", table_name="followup_request_users"
    )
    op.drop_table("followup_request_users")
    # ### end Alembic commands ###
