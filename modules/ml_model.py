from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_month(df):
    # df: Monthly summary with 'Month' and 'Amount'
    df['MonthNumber'] = np.arange(len(df))
    X = df['MonthNumber'].values.reshape(-1,1)
    y = df['Amount'].values
    model = LinearRegression()
    model.fit(X, y)
    next_month = np.array([[len(df)]])
    prediction = model.predict(next_month)[0]
    return round(prediction, 2)
