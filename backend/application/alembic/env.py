from logging.config import fileConfig
import os
from alembic import context

config = context.config
config.set_main_option('sqlalchemy.url',os.environ['DATABASE_URL'])