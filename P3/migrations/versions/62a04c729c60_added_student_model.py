"""Added Student model

Revision ID: 62a04c729c60
Revises: 3e75a59536e6
Create Date: 2022-09-14 17:41:50.201029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62a04c729c60'
down_revision = '3e75a59536e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(), nullable=True),
    sa.Column('student_email', sa.String(length=55), nullable=True),
    sa.Column('student_grade', sa.Integer(), nullable=True),
    sa.Column('student_birthday', sa.DateTime(), nullable=True),
    sa.Column('student_enrolled_date', sa.DateTime(), nullable=True),
    sa.CheckConstraint('student_grade BETWEEN 1 AND 12', name='grade_between_1_and_12'),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('student_email', name='unique_email')
    )
    op.create_index(op.f('ix_students_student_name'), 'students', ['student_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_student_name'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###
