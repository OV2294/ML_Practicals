# report.py
import pandas as pd
from datetime import datetime
import os

def generate_sales_report():
    # Sample data
    data = {
        'Product': ['Laptop', 'Phone', 'Tablet', 'Keyboard', 'Tshirt'],
        'Units Sold': [25, 40, 18, 22, 20],
        'Revenue': [25000, 20000, 9000, 500, 700]
    }

    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = rf"D:\AIMLK\reports\daily_sales_report_{timestamp}.csv"
    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the report
    df.to_csv(filename, index=False)
    print(f"✅ Report generated: {filename}")

if __name__ == "__main__":
    generate_sales_report()