"""add cover and review

Revision ID: d84b81b0faa0
Revises: f705b123d0b8
Create Date: 2022-06-20 23:43:20.577452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd84b81b0faa0'
down_revision = 'f705b123d0b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('covers',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('mime_type', sa.String(length=100), nullable=False),
    sa.Column('md5_hash', sa.String(length=100), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_covers_book_id_books')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_covers')),
    sa.UniqueConstraint('book_id', name=op.f('uq_covers_book_id')),
    sa.UniqueConstraint('md5_hash', name=op.f('uq_covers_md5_hash'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_reviews_book_id_books')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('covers')
    # ### end Alembic commands ###