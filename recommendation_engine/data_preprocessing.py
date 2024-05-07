import pandas as pd

# Read the CSV files into Pandas DataFrames
customers_df = pd.read_csv('data/customers.csv')
sales_df = pd.read_csv('data/sales.csv')
products_df = pd.read_csv('data/products.csv')

# data validation

# we only need to keep this important fields that gonna help us train our model and filter products with unvalidated values data
products_df = products_df[[ 'Uniqe Id', 'Product Name', 'Category', 'About Product' ]]
products_df = products_df[products_df[[ 'Uniqe Id', 'Product Name', 'Category', 'About Product' ]].notna().all(axis=1)]

# validate sales rows that only have a valid Interaction type and valid user_id and product_id
sales_df = sales_df[sales_df['Interaction type'].isin(['purchase', 'like', 'view'])]
sales_df = sales_df[sales_df[[ 'user id', 'product id']].notna().all(axis=1)]