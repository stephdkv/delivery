from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://hsofztuz:TBVw2WlZGLcrZGOb2YC5h-oQw-Sw8dXo@mouse.db.elephantsql.com/hsofztuz')
data_base_session = scoped_session(sessionmaker(bind = engine))

Base = declarative_base()
Base.query = data_base_session.query_property()