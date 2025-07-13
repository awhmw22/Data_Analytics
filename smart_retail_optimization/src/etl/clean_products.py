import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

def clean_products():
    engine = get_engine()
    products = pd.read_sql('SELECT * FROM "Products"', con=engine)

    print(f"Loaded {len(products)} product records")

    before = len(products)
    products = products[products['cost'] <= products['price']]
    after = len(products)
    print(f"Removed {before - after} products with cost > price")

    # Normalize category
    if 'category' in products.columns:
        products['category'] = products['category'].str.strip().str.title()

    # Save to new cleaned table
    products.to_sql("Clean_Products", con=engine, if_exists="replace", index=False)

    print(f"✅ Cleaned products saved: {len(products)} records")
    print(products.dtypes)


if __name__ == "__main__":
    clean_products()
