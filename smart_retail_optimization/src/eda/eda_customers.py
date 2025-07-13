import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

sns.set(style="whitegrid")

def eda_customers():
    engine = get_engine()
    customers = pd.read_sql('SELECT * FROM "Clean_Customers"', con=engine)
    print(f"✅ Loaded {len(customers)} clean customer records")

    # Convert data types
    customers['signup_date'] = pd.to_datetime(customers['signup_date'], errors='coerce')
    customers['age'] = pd.to_numeric(customers['age'], errors='coerce')

    # Basic stats
    print("\n📊 Data Summary:")
    print(customers.describe(include='all'))

    # Gender distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(data=customers, x='gender', palette='pastel')
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()

    # Age distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(customers['age'].dropna(), bins=20, kde=True, color='skyblue')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # Location distribution (top 10 cities)
    top_locations = customers['location'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_locations.values, y=top_locations.index, palette='viridis')
    plt.title("Top 10 Customer Locations")
    plt.xlabel("Number of Customers")
    plt.ylabel("City")
    plt.tight_layout()
    plt.show()

    # Sign-up trend over time
    if customers['signup_date'].notna().sum() > 0:
        monthly_signups = customers.groupby(pd.Grouper(key='signup_date', freq='M')).size()
        plt.figure(figsize=(12, 5))
        monthly_signups.plot(marker='o')
        plt.title("Monthly Customer Signups")
        plt.xlabel("Date")
        plt.ylabel("Number of Signups")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    eda_customers()
