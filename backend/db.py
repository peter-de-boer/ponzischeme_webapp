import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
if not uri:
    print("SQLALCHEMY_DATABASE_URI not defined")
else:
    print("SQLALCHEMY_DATABASE_URI is defined!!!")
    engine = create_engine(uri, echo=True)
    Base = declarative_base()


Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

"""
scoped_session: create a Session object that is basically globally available, i.e. whereever you do
import Session and session=Session(), session will always refer to the same object
so you can use that anywhere in the application, no need to pass the Session object!
"""

