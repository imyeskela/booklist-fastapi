import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from .base import metadata


books = Table(
    'books',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('title', String),
    Column('author', String, default='not found'),
    Column('written_date', String, default='not found'),
    Column('description', String, default='not found'),
)
