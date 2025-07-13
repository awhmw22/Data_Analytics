import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

def clean_customers():
    engine = get_engine()
    customers = pd.read_sql('SELECT * FROM "Customers"', con=engine)
    
    print(f"Loaded {len(customers)} customer records")
    
    # Drop duplicates
    customers.drop_duplicates(subset=['customer_id'], inplace=True)

    # Filter age: keep between 12 and 100
    customers = customers[(customers['age'] >= 12) & (customers['age'] <= 100)]

    # Normalize city names
    # Suppose it's 'location' instead of 'city'
    customers['location'] = customers['location'].str.strip().str.title()
 

    # Save clean data
    customers.to_sql('Clean_Customers', con=engine, if_exists='replace', index=False)
    
    print(f"✅ Cleaned customers saved: {len(customers)} records")

if __name__ == "__main__":
    clean_customers()
