"""shift users

Revision ID: 5bedad46562c
Revises: 0bc55992eb50
Create Date: 2022-03-29 16:25:21.812526

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "5bedad46562c"
down_revision = "0bc55992eb50"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shift_users",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("shift_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("admin", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["shift_id"], ["shifts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_shift_users_created_at"), "shift_users", ["created_at"], unique=False
    )
    op.create_index(
        "shift_users_forward_ind", "shift_users", ["shift_id", "user_id"], unique=True
    )
    op.create_index(
        "shift_users_reverse_ind", "shift_users", ["user_id", "shift_id"], unique=False
    )
    op.add_column("shifts", sa.Column("description", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("shifts", "description")
    op.drop_index("shift_users_reverse_ind", table_name="shift_users")
    op.drop_index("shift_users_forward_ind", table_name="shift_users")
    op.drop_index(op.f("ix_shift_users_created_at"), table_name="shift_users")
    op.drop_table("shift_users")
    # ### end Alembic commands ###
