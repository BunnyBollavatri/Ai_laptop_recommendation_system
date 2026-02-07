import pandas as pd
from db.connection import engine

print("🚀 Loading cleaned dataset...")

df = pd.read_csv("C:\\Users\\srivani\\Desktop\\Harsha_Project\\cleaned_laptops.csv")

df.to_sql(
    "laptops",
    engine,
    if_exists="replace",  # overwrite if exists
    index=False
)

print("🎉 Data successfully inserted into PostgreSQL!")
