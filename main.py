import logging
from extract import extract_users
from transform import transform_users
from load import load_to_postgres

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_etl():
    logging.info("ETL pipeline started")

    raw_df = extract_users()
    if raw_df.empty:
        logging.warning("No data extracted")
        return

    clean_df = transform_users(raw_df)
    if clean_df.empty:
        logging.warning("No data after transformation")
        return

    load_to_postgres(clean_df)
    logging.info("ETL pipeline finished successfully")

if __name__ == "__main__":
    run_etl()
