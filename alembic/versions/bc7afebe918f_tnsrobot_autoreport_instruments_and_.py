"""tnsrobot_autoreport_instruments_and_streams

Revision ID: bc7afebe918f
Revises: 0620901b0a2d
Create Date: 2023-09-01 11:04:10.517404

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "bc7afebe918f"
down_revision = "0620901b0a2d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "instrument_tnsrobots",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("instrument_id", sa.Integer(), nullable=False),
        sa.Column("tnsrobot_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["instrument_id"], ["instruments.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["tnsrobot_id"], ["tnsrobots.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "instrument_tnsrobots_forward_ind",
        "instrument_tnsrobots",
        ["instrument_id", "tnsrobot_id"],
        unique=True,
    )
    op.create_index(
        "instrument_tnsrobots_reverse_ind",
        "instrument_tnsrobots",
        ["tnsrobot_id", "instrument_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_instrument_tnsrobots_created_at"),
        "instrument_tnsrobots",
        ["created_at"],
        unique=False,
    )
    op.create_table(
        "stream_tnsrobots",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("stream_id", sa.Integer(), nullable=False),
        sa.Column("tnsrobot_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["stream_id"], ["streams.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["tnsrobot_id"], ["tnsrobots.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_stream_tnsrobots_created_at"),
        "stream_tnsrobots",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "stream_tnsrobots_forward_ind",
        "stream_tnsrobots",
        ["stream_id", "tnsrobot_id"],
        unique=True,
    )
    op.create_index(
        "stream_tnsrobots_reverse_ind",
        "stream_tnsrobots",
        ["tnsrobot_id", "stream_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("stream_tnsrobots_reverse_ind", table_name="stream_tnsrobots")
    op.drop_index("stream_tnsrobots_forward_ind", table_name="stream_tnsrobots")
    op.drop_index(op.f("ix_stream_tnsrobots_created_at"), table_name="stream_tnsrobots")
    op.drop_table("stream_tnsrobots")
    op.drop_index(
        op.f("ix_instrument_tnsrobots_created_at"), table_name="instrument_tnsrobots"
    )
    op.drop_index("instrument_tnsrobots_reverse_ind", table_name="instrument_tnsrobots")
    op.drop_index("instrument_tnsrobots_forward_ind", table_name="instrument_tnsrobots")
    op.drop_table("instrument_tnsrobots")
    # ### end Alembic commands ###
