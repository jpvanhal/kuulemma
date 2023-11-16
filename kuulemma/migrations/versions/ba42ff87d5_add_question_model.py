# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Add question model"""

# revision identifiers, used by Alembic.
revision = 'ba42ff87d5'
down_revision = '4c4f241e3bc'

import sqlalchemy as sa
from alembic import op



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_version',
    sa.Column('title', sa.Unicode(length=255), server_default='', autoincrement=False, nullable=True),
    sa.Column('lead', sa.UnicodeText(), server_default='', autoincrement=False, nullable=True),
    sa.Column('body', sa.UnicodeText(), server_default='', autoincrement=False, nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('hearing_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('main_image_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('position', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(op.f('ix_question_version_end_transaction_id'), 'question_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_question_version_operation_type'), 'question_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_question_version_transaction_id'), 'question_version', ['transaction_id'], unique=False)
    op.create_table('question',
    sa.Column('created_at', sa.DateTime(), server_default='now()', nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Unicode(length=255), server_default='', nullable=False),
    sa.Column('lead', sa.UnicodeText(), server_default='', nullable=False),
    sa.Column('body', sa.UnicodeText(), server_default='', nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hearing_id', sa.Integer(), nullable=True),
    sa.Column('main_image_id', sa.Integer(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hearing_id'], ['hearing.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['main_image_id'], ['image.id'], name='question_main_image_id_fkey', ondelete='CASCADE', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    #op.drop_table('spatial_ref_sys')
    op.add_column('comment', sa.Column('question_id', sa.Integer(), nullable=True))
    op.add_column('comment_version', sa.Column('question_id', sa.Integer(), autoincrement=False, nullable=True))
    op.add_column('image', sa.Column('question_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_image_question_id'), 'image', ['question_id'], unique=False)
    ### end Alembic commands ###

# unnamed constraints have to be edited manually!
    op.drop_constraint('comment_check', 'comment')
    op.create_check_constraint(
        'comment_check',
        'comment',
        '(comment.comment_id IS NOT NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.question_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NOT NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.question_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NOT NULL '
        'AND comment.section_id IS NULL '
        'AND comment.question_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NOT NULL '
        'AND comment.question_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.question_id IS NOT NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.question_id IS NULL '
        'AND comment.image_id IS NOT NULL) '
    )

    op.drop_constraint('image_check', 'image')
    op.create_check_constraint(
        'image_check',
        'image',
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NULL '
        'AND image.question_id IS NULL '
        'AND image.position IS NULL) '
        'OR '
        '(image.hearing_id IS NOT NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NULL '
        'AND image.question_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NOT NULL '
        'AND image.section_id IS NULL '
        'AND image.question_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NOT NULL '
        'AND image.question_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NULL '
        'AND image.question_id IS NOT NULL '
        'AND image.position >= 0) '
    )

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_question_id'), table_name='image')
    op.drop_column('image', 'question_id')
    op.drop_column('comment_version', 'question_id')
    op.drop_column('comment', 'question_id')
    '''
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    '''
    op.drop_table('question')
    op.drop_index(op.f('ix_question_version_transaction_id'), table_name='question_version')
    op.drop_index(op.f('ix_question_version_operation_type'), table_name='question_version')
    op.drop_index(op.f('ix_question_version_end_transaction_id'), table_name='question_version')
    op.drop_table('question_version')
    ### end Alembic commands ###

    # unnamed constraints have to be edited manually!
    op.drop_constraint('comment_check', 'comment')
    op.create_check_constraint(
        'comment_check',
        'comment',
        '(comment.comment_id IS NOT NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NOT NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NOT NULL '
        'AND comment.section_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NOT NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.alternative_id IS NULL '
        'AND comment.section_id IS NULL '
        'AND comment.image_id IS NOT NULL) '
    )

    op.drop_constraint('image_check', 'image')
    op.create_check_constraint(
        'image_check',
        'image',
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NULL '
        'AND image.position IS NULL) '
        'OR '
        '(image.hearing_id IS NOT NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NOT NULL '
        'AND image.section_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.alternative_id IS NULL '
        'AND image.section_id IS NOT NULL '
        'AND image.position >= 0) '
    )