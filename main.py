from etl.extract import extract_csv
from etl.transform import clean_sales_data, clean_customer_data
from etl.load import load_to_postgresql

# Paths
sales_path = 'data/daily_sales.csv'
customer_path = 'data/customer.csv'

# ETL Steps 
# E and T // can skip E if directly added
sales_df = clean_sales_data(extract_csv(sales_path))  # you can directly add pd.read_csv(data/daily_sales.csv) 
customer_df = clean_customer_data(extract_csv(customer_path))

# L
load_to_postgresql(customer_df, 'customers')
load_to_postgresql(sales_df, 'sales')

print("✅ ETL completed.")
