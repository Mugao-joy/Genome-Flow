from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://genomeflow:genomeflow@localhost:5432/genomeflow"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
