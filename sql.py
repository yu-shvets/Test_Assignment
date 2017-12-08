import json
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Deserializing json file
with open('proxies.json') as data_file:
    data = json.load(data_file)

data = data[:-5 or None]
hosts =[i['host'] for i in data if i['host']]


#Creating and populating Sqlite database using SQlAlchemy
engine = create_engine('sqlite:///proxies.db', echo=True)
Base = declarative_base()

class Proxies(Base):
    __tablename__ = "proxies"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String)

Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

for host in hosts:
    new_host = Proxies(ip_address=host)
    session.add(new_host)

session.commit()

