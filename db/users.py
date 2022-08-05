import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime
from .base import metadata


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('email', String, primary_key=True, unique=True),
    Column('hashed_password', String),
    Column('created_date', DateTime, default=datetime.datetime.utcnow())
)
