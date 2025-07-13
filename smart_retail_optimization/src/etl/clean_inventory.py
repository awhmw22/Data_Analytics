import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

def clean_inventory():
    engine = get_engine()
    inventory = pd.read_sql('SELECT * FROM "Inventory"', con=engine)
    products = pd.read_sql('SELECT product_id FROM "Products"', con=engine)

    print(f"Loaded {len(inventory)} inventory records")

    # Drop duplicates
    #inventory.drop_duplicates(subset=['inventory_id'], inplace=True)

    # Remove negative stock
    inventory = inventory[inventory['stock_level'] >= 0]

    # Ensure product_id exists
    inventory = inventory[inventory['product_id'].isin(products['product_id'])]

    # Save
    inventory.to_sql('Clean_Inventory', con=engine, if_exists='replace', index=False)

    print(f"✅ Cleaned inventory saved: {len(inventory)} records")

if __name__ == "__main__":
    clean_inventory()
