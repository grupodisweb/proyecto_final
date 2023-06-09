"""datos iniciales

Revision ID: 27c100eeb09e
Revises: d6ae83f45e44
Create Date: 2023-07-03 19:08:23.405686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27c100eeb09e'
down_revision = 'd6ae83f45e44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Noticias', schema=None) as batch_op:
        batch_op.alter_column('categoria',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=16),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Noticias', schema=None) as batch_op:
        batch_op.alter_column('categoria',
               existing_type=sa.String(length=16),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    # ### end Alembic commands ###
