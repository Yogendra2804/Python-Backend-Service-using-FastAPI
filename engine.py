from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(
    "sqlite:///D:/Coding laungages/python/Base/sequal_light/Database/database1.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

# SessionLocal = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)
session = Session()