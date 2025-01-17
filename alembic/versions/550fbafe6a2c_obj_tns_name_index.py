"""obj_tns_name_index

Revision ID: 550fbafe6a2c
Revises: 1d0d58fe42fe
Create Date: 2024-02-10 13:55:19.094894

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "550fbafe6a2c"
down_revision = "1d0d58fe42fe"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_objs_tns_name"), "objs", ["tns_name"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_objs_tns_name"), table_name="objs")
    # ### end Alembic commands ###
