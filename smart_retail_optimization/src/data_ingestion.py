import pandas as pd
from utils import get_engine

def load_csv_to_db(csv_path, table_name, if_exists='append'):
    engine = get_engine()
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} records from {csv_path}")
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
    print(f"Inserted data into {table_name}")

if __name__ == "__main__":
    # Example: load products
    load_csv_to_db("../data/raw/products.csv", "Products")
    load_csv_to_db("../data/raw/suppliers.csv", "Suppliers")
    load_csv_to_db("../data/raw/customers.csv", "Customers")
    load_csv_to_db("../data/raw/stores.csv", "Stores")
    load_csv_to_db("../data/raw/sales.csv", "Sales")
    load_csv_to_db("../data/raw/inventory.csv", "Inventory")
