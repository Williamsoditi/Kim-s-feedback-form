"""Initial migration

Revision ID: f22330141c37
Revises: 
Create Date: 2022-05-21 00:23:58.287150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f22330141c37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('context', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('feedback_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delete',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('downvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('password_secure', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('upvote')
    op.drop_table('downvote')
    op.drop_table('delete')
    op.drop_table('comments')
    op.drop_table('roles')
    op.drop_table('feedbacks')
    # ### end Alembic commands ###
