import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker('en_PK')  # Pakistan locale

# Config
NUM_PRODUCTS = 500
NUM_SUPPLIERS = 20
NUM_STORES = 50
NUM_CUSTOMERS = 30000
NUM_SALES = 100000

# 1️⃣ Generate suppliers
def generate_suppliers():
    suppliers = []
    for i in range(1, NUM_SUPPLIERS + 1):
        suppliers.append({
            "supplier_id": i,
            "name": fake.company(),
            "contact": fake.email()
        })
    return pd.DataFrame(suppliers)

# 2️⃣ Generate products
def generate_products():
    categories = ['Electronics', 'Fashion', 'Groceries', 'Furniture', 'Toys']
    products = []
    for i in range(1, NUM_PRODUCTS + 1):
        products.append({
            "product_id": i,
            "name": f"{fake.word().capitalize()} {random.choice(['Pro', 'Max', 'Lite', 'Plus'])}",
            "category": random.choice(categories),
            "price": round(random.uniform(100, 100000), 2),
            "cost": round(random.uniform(50, 80000), 2),
            "supplier_id": random.randint(1, NUM_SUPPLIERS)
        })
    return pd.DataFrame(products)

# 3️⃣ Generate stores
def generate_stores():
    cities = ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Peshawar', 'Multan', 'Faisalabad', 'Quetta', 'Hyderabad']
    sizes = ['Small', 'Medium', 'Large']
    stores = []
    for i in range(1, NUM_STORES + 1):
        stores.append({
            "store_id": i,
            "name": f"{fake.company()} Store",
            "location": random.choice(cities),
            "size": random.choice(sizes)
        })
    return pd.DataFrame(stores)

# 4️⃣ Generate customers
def generate_customers():
    customers = []
    for i in range(1, NUM_CUSTOMERS + 1):
        customers.append({
            "customer_id": i,
            "name": fake.name(),
            "age": random.randint(18, 65),
            "gender": random.choice(['Male', 'Female']),
            "location": fake.city(),
            "signup_date": fake.date_between(start_date='-3y', end_date='today')
        })
    return pd.DataFrame(customers)

# 5️⃣ Generate sales
def generate_sales():
    sales = []
    for i in range(1, NUM_SALES + 1):
        sales.append({
            "sale_id": i,
            "product_id": random.randint(1, NUM_PRODUCTS),
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "date": fake.date_time_between(start_date='-1y', end_date='now'),
            "quantity": random.randint(1, 5),
            "store_id": random.choice([random.randint(1, NUM_STORES), None]),
            "channel": random.choice(['in-store', 'online'])
        })
    return pd.DataFrame(sales)

# 6️⃣ Generate inventory
def generate_inventory(products_df, stores_df):
    inventory = []
    for _, store in stores_df.iterrows():
        for _, product in products_df.sample(50).iterrows():
            inventory.append({
                "product_id": product['product_id'],
                "store_id": store['store_id'],
                "stock_level": random.randint(0, 200),
                "last_restock_date": fake.date_between(start_date='-6mo', end_date='today')
            })
    return pd.DataFrame(inventory)

# 📝 Save all to CSV
def save_all():
    suppliers = generate_suppliers()
    products = generate_products()
    stores = generate_stores()
    customers = generate_customers()
    sales = generate_sales()
    inventory = generate_inventory(products, stores)

    suppliers.to_csv("../data/raw/suppliers.csv", index=False)
    products.to_csv("../data/raw/products.csv", index=False)
    stores.to_csv("../data/raw/stores.csv", index=False)
    customers.to_csv("../data/raw/customers.csv", index=False)
    sales.to_csv("../data/raw/sales.csv", index=False)
    inventory.to_csv("../data/raw/inventory.csv", index=False)

    print("✅ All CSVs generated successfully!")

if __name__ == "__main__":
    save_all()
