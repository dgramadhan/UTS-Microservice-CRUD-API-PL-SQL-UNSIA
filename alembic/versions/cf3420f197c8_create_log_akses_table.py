"""create log_akses table

Revision ID: cf3420f197c8
Revises: f25b0f31ea19
Create Date: 2023-12-07 16:44:14.563809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf3420f197c8'
down_revision: Union[str, None] = 'f25b0f31ea19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        '''
        CREATE TABLE log_access (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            status VARCHAR(255) NOT NULL,
            login_date TIMESTAMP NOT NULL
        )
        '''
    )


def downgrade() :
    op.execute('DROP TABLE log_access')
