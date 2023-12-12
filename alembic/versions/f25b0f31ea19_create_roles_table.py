"""create roles table

Revision ID: f25b0f31ea19
Revises: 259e901aa4b9
Create Date: 2023-12-07 16:42:53.167431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f25b0f31ea19'
down_revision: Union[str, None] = '259e901aa4b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        '''
        CREATE TABLE roles (
            id SERIAL PRIMARY KEY,
            role_name VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL
        )
        '''
    )


def downgrade() :
    op.execute('DROP TABLE roles')
