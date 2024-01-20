from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()
