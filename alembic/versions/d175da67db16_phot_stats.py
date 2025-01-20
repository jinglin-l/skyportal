"""phot_stats

Revision ID: d175da67db16
Revises: 438a795cbd15
Create Date: 2022-06-15 13:55:53.241873

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "d175da67db16"
down_revision = "438a795cbd15"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "photstats",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified", sa.DateTime(), nullable=False),
        sa.Column("last_update", sa.DateTime(), nullable=True),
        sa.Column("last_full_update", sa.DateTime(), nullable=True),
        sa.Column("obj_id", sa.String(), nullable=False),
        sa.Column("num_obs_global", sa.Integer(), nullable=False),
        sa.Column(
            "num_obs_per_filter", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("num_det_global", sa.Integer(), nullable=False),
        sa.Column(
            "num_det_per_filter", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("first_detected_mjd", sa.Float(), nullable=True),
        sa.Column("first_detected_mag", sa.Float(), nullable=True),
        sa.Column("first_detected_filter", sa.String(), nullable=True),
        sa.Column("last_detected_mjd", sa.Float(), nullable=True),
        sa.Column("last_detected_mag", sa.Float(), nullable=True),
        sa.Column("last_detected_filter", sa.String(), nullable=True),
        sa.Column("recent_obs_mjd", sa.Float(), nullable=True),
        sa.Column("last_non_detection_mjd", sa.Float(), nullable=True),
        sa.Column("time_to_non_detection", sa.Float(), nullable=True),
        sa.Column("mean_mag_global", sa.Float(), nullable=True),
        sa.Column(
            "mean_mag_per_filter",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("mean_color", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("peak_mag_global", sa.Float(), nullable=True),
        sa.Column("peak_mjd_global", sa.Float(), nullable=True),
        sa.Column(
            "peak_mag_per_filter",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "peak_mjd_per_filter",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("faintest_mag_global", sa.Float(), nullable=True),
        sa.Column(
            "faintest_mag_per_filter",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("deepest_limit_global", sa.Float(), nullable=True),
        sa.Column(
            "deepest_limit_per_filter",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("rise_rate", sa.Float(), nullable=True),
        sa.Column("decay_rate", sa.Float(), nullable=True),
        sa.Column("mag_rms_global", sa.Float(), nullable=True),
        sa.Column(
            "mag_rms_per_filter", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.ForeignKeyConstraint(["obj_id"], ["objs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_photstats_created_at"), "photstats", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_photstats_decay_rate"), "photstats", ["decay_rate"], unique=False
    )
    op.create_index(
        op.f("ix_photstats_deepest_limit_global"),
        "photstats",
        ["deepest_limit_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_deepest_limit_per_filter"),
        "photstats",
        ["deepest_limit_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_faintest_mag_global"),
        "photstats",
        ["faintest_mag_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_faintest_mag_per_filter"),
        "photstats",
        ["faintest_mag_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_first_detected_filter"),
        "photstats",
        ["first_detected_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_first_detected_mag"),
        "photstats",
        ["first_detected_mag"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_first_detected_mjd"),
        "photstats",
        ["first_detected_mjd"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_detected_filter"),
        "photstats",
        ["last_detected_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_detected_mag"),
        "photstats",
        ["last_detected_mag"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_detected_mjd"),
        "photstats",
        ["last_detected_mjd"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_full_update"),
        "photstats",
        ["last_full_update"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_non_detection_mjd"),
        "photstats",
        ["last_non_detection_mjd"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_last_update"), "photstats", ["last_update"], unique=False
    )
    op.create_index(
        op.f("ix_photstats_mag_rms_global"),
        "photstats",
        ["mag_rms_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_mag_rms_per_filter"),
        "photstats",
        ["mag_rms_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_mean_color"), "photstats", ["mean_color"], unique=False
    )
    op.create_index(
        op.f("ix_photstats_mean_mag_global"),
        "photstats",
        ["mean_mag_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_mean_mag_per_filter"),
        "photstats",
        ["mean_mag_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_num_det_global"),
        "photstats",
        ["num_det_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_num_det_per_filter"),
        "photstats",
        ["num_det_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_num_obs_global"),
        "photstats",
        ["num_obs_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_num_obs_per_filter"),
        "photstats",
        ["num_obs_per_filter"],
        unique=False,
    )
    op.create_index(op.f("ix_photstats_obj_id"), "photstats", ["obj_id"], unique=False)
    op.create_index(
        op.f("ix_photstats_peak_mag_global"),
        "photstats",
        ["peak_mag_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_peak_mag_per_filter"),
        "photstats",
        ["peak_mag_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_peak_mjd_global"),
        "photstats",
        ["peak_mjd_global"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_peak_mjd_per_filter"),
        "photstats",
        ["peak_mjd_per_filter"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_recent_obs_mjd"),
        "photstats",
        ["recent_obs_mjd"],
        unique=False,
    )
    op.create_index(
        op.f("ix_photstats_rise_rate"), "photstats", ["rise_rate"], unique=False
    )
    op.create_index(
        op.f("ix_photstats_time_to_non_detection"),
        "photstats",
        ["time_to_non_detection"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_photstats_time_to_non_detection"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_rise_rate"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_recent_obs_mjd"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_peak_mjd_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_peak_mjd_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_peak_mag_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_peak_mag_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_obj_id"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_num_obs_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_num_obs_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_num_det_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_num_det_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_mean_mag_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_mean_mag_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_mean_color"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_mag_rms_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_mag_rms_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_update"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_non_detection_mjd"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_full_update"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_detected_mjd"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_detected_mag"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_last_detected_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_first_detected_mjd"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_first_detected_mag"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_first_detected_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_faintest_mag_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_faintest_mag_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_deepest_limit_per_filter"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_deepest_limit_global"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_decay_rate"), table_name="photstats")
    op.drop_index(op.f("ix_photstats_created_at"), table_name="photstats")
    op.drop_table("photstats")
    # ### end Alembic commands ###
