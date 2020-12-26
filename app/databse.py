from typing import List

import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import asyncio
import concurrent

BASE = declarative_base()

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("energy", sqlalchemy.FLOAT),
    sqlalchemy.Column("health", sqlalchemy.Integer),
    sqlalchemy.Column("attack", sqlalchemy.Integer),
    sqlalchemy.Column("defense", sqlalchemy.Integer),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


async def get_user_from_database(user):
    query = users.select().where(users.c.id == user.id)
    res = await database.fetch_one(query)
    if not res:
        command = users.insert().values(id=user.id, name = user.name, attack= 10, defense=0, health=100, energy=100)
        await database.execute(command)
        query = users.select().where(users.c.id==user.id)
        res = await database.fetch_one(query)
    return res

async def add_energy_to_users():
    query = users.select()
    res = await database.fetch_all(query)
    for r in res:
        current_energy = r.energy
        new_energy = min(100, current_energy+0.00115)
        command = users.update().where(users.c.id==r.id).values(energy=new_energy)
        await database.execute(command)

async def status_task():
    while True:
        await add_energy_to_users()
        await asyncio.sleep(1)

if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(add_energy_to_users())