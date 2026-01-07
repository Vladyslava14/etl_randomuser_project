import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

loaded = load_dotenv()
print("dotenv loaded:", loaded)


def load_to_postgres(df):
    try:
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        db = os.getenv("POSTGRES_DB")

        if not all([user,password,host,port, db]):
            raise ValueError("Missing PostgreSQL environment variables")

        conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"    
        
        engine = create_engine(conn_str)

        logging.info(f"Loading {len(df)} records to PostgreSQL")


        df.to_sql(
        "users",
        engine,
        if_exists="append",
        index=False,
        method="multi"
        )

        logging.info("Data successfully loaded to PostreSQL")

    except Exception as e:
        logging.error(f"Error while loading to PostgreSQL: {e}")
        raise
