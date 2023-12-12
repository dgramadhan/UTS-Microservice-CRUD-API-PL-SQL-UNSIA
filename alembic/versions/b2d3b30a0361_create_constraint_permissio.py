"""create constraint permissio

Revision ID: b2d3b30a0361
Revises: cf3420f197c8
Create Date: 2023-12-07 17:00:53.132953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2d3b30a0361'
down_revision: Union[str, None] = 'cf3420f197c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.execute(
        '''
            ALTER TABLE permissions 
            ADD CONSTRAINT fk_permission_user_id FOREIGN KEY (user_id) REFERENCES users(id)
        '''
    )
    op.execute(
    '''
        ALTER TABLE permissions 
        ADD CONSTRAINT fk_permission_role_id FOREIGN KEY (role_id) REFERENCES roles(id)
    ''')


def downgrade() :
    op.execute('ALTER TABLE permissions DROP CONSTRAINT fk_permission_user_id')
    op.execute('ALTER TABLE permissions DROP CONSTRAINT fk_permission_role_id')