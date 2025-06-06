"""Add image_url to Pokemon model

Revision ID: f7232aba3254
Revises: 513a78645f17
Create Date: 2025-05-09 10:38:17.661288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7232aba3254'
down_revision = '513a78645f17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('image_url', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemon', 'image_url')
    # ### end Alembic commands ###
