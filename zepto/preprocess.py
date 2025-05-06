import pandas as pd

def preprocess_data(df):
    """Clean and enhance the dataset"""
    if df is None:
        return None

    numeric_cols = ['mrp', 'discountpercent', 'availablequantity', 'quantity', 'weightingms']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    if all(col in df.columns for col in ['mrp', 'discountpercent', 'quantity']):
        df['selling_price'] = df['mrp'] * (1 - df['discountpercent']/100)
        df['revenue'] = df['selling_price'] * df['quantity']

    if 'outofstock' in df.columns:
        df['in_stock'] = ~df['outofstock'].astype(bool)

    return df
