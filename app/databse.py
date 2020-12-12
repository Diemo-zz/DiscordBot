from typing import List

import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, FLOAT, String, CheckConstraint
from pydantic import BaseModel

BASE = declarative_base()

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("health", sqlalchemy.Integer),
    sqlalchemy.Column("attack", sqlalchemy.Integer),
    sqlalchemy.Column("defense", sqlalchemy.Integer),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


async def get_user_from_database(user):
    query = users.select().where(users.c.id==user.id)
    res = await database.fetch_one(query)
    if not res:
        command = users.insert().values(id=user.id, name = user.name, attack= 10, defense=50, health=100)
        await database.execute(command)
        query = users.select().where(users.c.id==user.id)
        res = await database.fetch_one(query)
    return res
