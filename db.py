from sqlalchemy import Column, String, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import atexit

PG_DSN = "postgresql://app:1234@127.0.0.1:6000/ads"

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creator = Column(String, nullable=False)
    date = Column(DateTime, server_default=func.now())


Base.metadata.create_all(bind=engine)
