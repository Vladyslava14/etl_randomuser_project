import pandas as pd

def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    df = df[
        [
            "login.uuid",
            "gender",
            "name.first",
            "name.last",
            "dob.date",
            "dob.age",

            "location.street.number",
            "location.street.name",
            "location.city",
            "location.state",
            "location.country",
            "location.postcode",

            "location.coordinates.latitude",
            "location.coordinates.longitude",

            "email",
            "phone",
            "cell",
            "nat"
        ]
    ].copy()

    df.columns = [
        "user_id",
        "gender",
        "first_name",
        "last_name",
        "date_of_birth",
        "age",

        "street_number",
        "street_name",
        "city",
        "state",
        "country",
        "postcode",

        "latitude",
        "longitude",

        "email",
        "phone",
        "cell",
        "nationality"
    ]

    # типізація
    df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
    df["age"] = df["age"].astype(int)

    df["latitude"] = df["latitude"].astype(float)
    df["longitude"] = df["longitude"].astype(float)

    # cleaning
    df = df.drop_duplicates(subset="user_id")
    df = df.dropna(subset=["country", "city"])

    return df
    print(transform_users)
