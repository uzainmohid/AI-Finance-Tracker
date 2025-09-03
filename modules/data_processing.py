import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df['Amount'] = df['Amount'].astype(float)
    return df

def categorize_expenses(df):
    # Already has Category column, just for demo
    return df.groupby('Category')['Amount'].sum().reset_index()

def monthly_summary(df):
    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby('Month')['Amount'].sum().reset_index()
    return summary
