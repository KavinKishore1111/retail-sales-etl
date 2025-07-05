import pandas as pd;


# Cleaning the data 

def clean_sales_data(df):
    df.dropna(inplace=True)
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['sale_amount'] = df['sale_amount'].replace(r'[\$,]', '', regex=True)

    return df

def clean_customer_data(df):
    df.dropna(inplace=True)
    return df


