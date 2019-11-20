"""add versioned instance config

Revision ID: 523fff3f969c
Revises: 3da3fcab826a
Create Date: 2019-11-02 23:06:12.161868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523fff3f969c'
down_revision = '3da3fcab826a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instance_config',
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('valid_until', sa.DateTime(), nullable=True),
    sa.Column('allow_document_uploads', sa.Boolean(), nullable=True),

    sa.PrimaryKeyConstraint('version'),
    sa.UniqueConstraint('valid_until'),
    )
    # ### end Alembic commands ###

    # Data migration:  Since allow_document_uploads is the first
    # instance_config setting (column), all we have to do is insert a
    # row with its default value.
    conn = op.get_bind()
    conn.execute("""INSERT INTO instance_config (allow_document_uploads) VALUES (1)""")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instance_config')
    # ### end Alembic commands ###
