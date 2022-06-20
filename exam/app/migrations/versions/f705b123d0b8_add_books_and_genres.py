"""add books and genres

Revision ID: f705b123d0b8
Revises: b436b1ea7def
Create Date: 2022-06-20 23:33:58.902882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f705b123d0b8'
down_revision = 'b436b1ea7def'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('year', sa.Date(), nullable=False),
    sa.Column('publisher', sa.String(length=30), nullable=False),
    sa.Column('author', sa.String(length=30), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books')),
    sa.UniqueConstraint('title', name=op.f('uq_books_title'))
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_genres')),
    sa.UniqueConstraint('genre_name', name=op.f('uq_genres_genre_name'))
    )
    op.create_table('books_genres',
    sa.Column('books_id', sa.Integer(), nullable=False),
    sa.Column('genres_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['books_id'], ['books.id'], name=op.f('fk_books_genres_books_id_books')),
    sa.ForeignKeyConstraint(['genres_id'], ['genres.id'], name=op.f('fk_books_genres_genres_id_genres')),
    sa.PrimaryKeyConstraint('books_id', 'genres_id', name=op.f('pk_books_genres'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_genres')
    op.drop_table('genres')
    op.drop_table('books')
    # ### end Alembic commands ###