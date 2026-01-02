import requests
import pandas as pd

def extract_users(results=500):
    url = f"https://randomuser.me/api/?results={results}"
    response = requests.get(url)
    data = response.json()
    return pd.json_normalize(data["results"])
df = extract_users(10)
print(df.head())  
    