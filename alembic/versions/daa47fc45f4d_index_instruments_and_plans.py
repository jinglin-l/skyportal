"""index instruments and plans

Revision ID: daa47fc45f4d
Revises: f870b311df53
Create Date: 2022-11-28 15:06:30.056571

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'daa47fc45f4d'
down_revision = '8bd7883f99bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f('ix_instrumentfieldtiles_instrument_id'),
        'instrumentfieldtiles',
        ['instrument_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_plannedobservations_field_id'),
        'plannedobservations',
        ['field_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_plannedobservations_observation_plan_id'),
        'plannedobservations',
        ['observation_plan_id'],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f('ix_plannedobservations_observation_plan_id'),
        table_name='plannedobservations',
    )
    op.drop_index(
        op.f('ix_plannedobservations_field_id'), table_name='plannedobservations'
    )
    op.drop_index(
        op.f('ix_instrumentfieldtiles_instrument_id'), table_name='instrumentfieldtiles'
    )
    # ### end Alembic commands ###