"""Make Annotation.data non-nullable

Revision ID: c867ada3e0c4
Revises: 19b72aac66cd
Create Date: 2021-04-12 15:13:26.070329

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "c867ada3e0c4"
down_revision = "19b72aac66cd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "annotations",
        "data",
        existing_type=postgresql.JSONB(astext_type=sa.Text()),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "annotations",
        "data",
        existing_type=postgresql.JSONB(astext_type=sa.Text()),
        nullable=True,
    )
    # ### end Alembic commands ###
