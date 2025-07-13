import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_engine

def eda_products():
    engine = get_engine()
    products = pd.read_sql('SELECT * FROM "Clean_Products"', con=engine)

    print(f"Loaded {len(products)} clean product records")

    # Profit margin calculation
    products['profit_margin'] = products['price'] - products['cost']
    products['profit_percent'] = ((products['price'] - products['cost']) / products['cost']) * 100

    print(products.describe())

    # Top 10 most profitable products
    top_profit = products.sort_values(by='profit_margin', ascending=False).head(10)
    print("\nTop 10 Most Profitable Products:")
    print(top_profit[['name', 'price', 'cost', 'profit_margin', 'profit_percent']])

    # Category distribution
    if 'category' in products.columns:
        category_counts = products['category'].value_counts()
        print("\nCategory Distribution:")
        print(category_counts)

        # Visual
        sns.countplot(y='category', data=products, order=category_counts.index)
        plt.title('Number of Products per Category')
        plt.tight_layout()
        plt.show()

    # Profitability distribution
    sns.histplot(products['profit_percent'], bins=30, kde=True)
    plt.title('Distribution of Profit Percent')
    plt.xlabel('Profit %')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    eda_products()
