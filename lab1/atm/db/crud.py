from lab1.atm.db.config import DATABASE_URI
from lab1.atm.db.Models import Card

import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

engine = sql.create_engine(DATABASE_URI)

try:
    engine.connect()
except SQLAlchemyError as err:
    print('Connection refused.\nCheck connection')
    exit(1)

session = sessionmaker(bind=engine)
