from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import settings

engine = create_engine(f'postgresql://{settings.LOGIN}:{settings.PASSWORD}@{settings.POSTGRES_URL}/{settings.DB_NAME}')
data_base_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = data_base_session.query_property()
