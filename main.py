import sqlalchemy
from sqlalchemy import create_engine, MetaData
import db_creation

print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:root@localhost/rdbs", echo=True,future=True)

metadata = MetaData() # hlavní objekt

db_creation.create_db(engine, metadata)
