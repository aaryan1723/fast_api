from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

my_sql_url='mysql+pymysql://root:123456@localhost:3306/blogapplication'
engine=create_engine(my_sql_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

base=declarative_base()