from sqlalchemy import create_engine

def load_to_postgres(df):
    engine = create_engine(
        "postgresql+psycopg2://postgres:...@localhost:5432/user_db"
    )

    df.to_sql(
    "users",
    engine,
    if_exists="append",
    index=False,
    method="multi"
)
print("successfully")
