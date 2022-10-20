import sqlalchemy
import psycopg2
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData, ForeignKey
#from sqlalchemy.orm import declarative_base, sessionmaker, relationship

import db_creation

print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:root@localhost/rdbs", future=True)
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

#connection = engine.connect()
#connection.connection.connection
metadata = MetaData()#  hlavní objekt

db_creation.create_db(engine, metadata)
