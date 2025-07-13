import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

def clean_sales():
    engine = get_engine()
    
    # Load sales data
    sales = pd.read_sql('SELECT * FROM "Sales"', con=engine)
    
    print(f"Loaded {len(sales)} sales records")
    
    # Remove duplicates
    sales.drop_duplicates(subset=['sale_id'], inplace=True)
    
    # Remove sales with negative quantity or price (if price info is there)
    sales = sales[sales['quantity'] > 0]
    
    # Convert 'date' to datetime
    sales['date'] = pd.to_datetime(sales['date'], errors='coerce')

# Now remove rows where date is in the future
    sales = sales[sales['date'] <= pd.Timestamp.now()]

# Also drop rows where date conversion failed (became NaT)
    sales = sales.dropna(subset=['date'])

    
    # Fill null store_id as 0 (or keep as NULL if that’s your business rule)
    sales['store_id'] = sales['store_id'].fillna(0)
    
    # Create calculated column: sale_amount (price * quantity)
    # Join with Products to get price
    products = pd.read_sql('SELECT product_id, price FROM "Products"', con=engine)
    sales = sales.merge(products, on='product_id', how='left')
    sales['sale_amount'] = sales['price'] * sales['quantity']
    
    # Save cleaned data to DB
    sales.to_sql('Clean_Sales', con=engine, if_exists='replace', index=False)
    
    print(f"✅ Cleaned sales saved: {len(sales)} records")

if __name__ == "__main__":
    clean_sales()
