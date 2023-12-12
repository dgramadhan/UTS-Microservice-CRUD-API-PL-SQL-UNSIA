"""create permission table

Revision ID: 259e901aa4b9
Revises: 76dea366c4a9
Create Date: 2023-12-07 16:38:07.377373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '259e901aa4b9'
down_revision: Union[str, None] = '76dea366c4a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        '''
        CREATE TABLE permissions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            role_id INTEGER NOT NULL
        )
        '''
    )


def downgrade() :
    op.execute('DROP TABLE permissions')
