import pandas as pd
import ast

print("🚀 Starting data cleaning pipeline...")

# ---------------------------------
# LOAD DATASET
# ---------------------------------

try:
    df = pd.read_csv("backend\data\Flipkart laptop data.csv")
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print("❌ Failed to load dataset:", e)
    exit()

print("Original Shape:", df.shape)


# ---------------------------------
# DROP USELESS COLUMN
# ---------------------------------

if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)


# ---------------------------------
# RENAME COLUMNS
# ---------------------------------

df.rename(columns={
    "NAME": "name",
    "DISCOUNTED PRICE": "price",
    "ACTUAL PRICE": "actual_price",
    "OTHER PROPERTIES": "specs"
}, inplace=True)


# ---------------------------------
# CLEAN PRICE
# ---------------------------------

def clean_price(col):
    return (
        col.astype(str)
        .str.replace(r"[^\d]", "", regex=True)
        .replace("", "0")
        .astype(int)
    )

df["price"] = clean_price(df["price"])
df["actual_price"] = clean_price(df["actual_price"])


# ---------------------------------
# REMOVE NULL SPECS BEFORE PARSING
# ---------------------------------

df = df[df["specs"].notna()]


# ---------------------------------
# CONVERT STRING -> LIST
# ---------------------------------

def safe_literal_eval(val):
    try:
        return ast.literal_eval(val)
    except:
        return []

df["specs"] = df["specs"].apply(safe_literal_eval)


# ---------------------------------
# EXTRACT RAM
# ---------------------------------

def extract_ram(specs):
    for item in specs:
        if "RAM" in item.upper():
            numbers = ''.join(filter(str.isdigit, item))
            if numbers:
                return int(numbers)
    return None

df["ram"] = df["specs"].apply(extract_ram)


# ---------------------------------
# EXTRACT STORAGE
# ---------------------------------

def extract_storage(specs):
    for item in specs:
        if "SSD" in item.upper() or "HDD" in item.upper():
            numbers = ''.join(filter(str.isdigit, item))
            if numbers:
                return int(numbers)
    return None

df["storage"] = df["specs"].apply(extract_storage)


# ---------------------------------
# EXTRACT CPU
# ---------------------------------

def extract_cpu(specs):
    for item in specs:
        if "PROCESSOR" in item.upper():
            return item
    return "Unknown"

df["cpu"] = df["specs"].apply(extract_cpu)


# ---------------------------------
# EXTRACT BRAND
# ---------------------------------

df["brand"] = df["name"].str.split().str[0]


# ---------------------------------
# REMOVE DUPLICATES
# ---------------------------------

df.drop_duplicates(subset=["name", "price"], inplace=True)


# ---------------------------------
# DROP BAD ROWS
# ---------------------------------

df.dropna(subset=["ram", "price"], inplace=True)


# ---------------------------------
# FINAL DATASET
# ---------------------------------

df = df[[
    "brand",
    "name",
    "price",
    "actual_price",
    "ram",
    "storage",
    "cpu"
]]

print("✅ Cleaned Shape:", df.shape)


# ---------------------------------
# SAVE CLEAN DATA
# ---------------------------------

output_path = "cleaned_laptops.csv"


df.to_csv(output_path, index=False)

print("🎉 CLEANING COMPLETE!")
print("Saved to:", output_path)
