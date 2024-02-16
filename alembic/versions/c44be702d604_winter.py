"""winter

Revision ID: c44be702d604
Revises: 93a04c1fb3a7
Create Date: 2024-01-31 11:44:39.089204

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'c44be702d604'
down_revision = '93a04c1fb3a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # add WINTERAPI in the right place
    with op.get_context().autocommit_block():
        op.execute(
            "ALTER TYPE followup_apis ADD VALUE IF NOT EXISTS 'WINTERAPI' AFTER 'TESSAPI'"
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
