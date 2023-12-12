"""create users table

Revision ID: 76dea366c4a9
Revises: 2a424e35d30f
Create Date: 2023-12-07 16:35:01.927638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76dea366c4a9'
down_revision: Union[str, None] = '2a424e35d30f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():  
    op.execute(
        '''
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            phone_number VARCHAR(255) NOT NULL
        );
        '''
    )


def downgrade() :
     op.execute('DROP TABLE users;')