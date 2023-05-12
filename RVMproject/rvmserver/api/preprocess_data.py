import numpy as np
import pandas as pd

def preprocess_data(data):
    # Convert data to Pandas DataFrame
    df = pd.DataFrame(data, columns=['value'])
    
    # Convert date strings to datetime objects
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    
    # Set date column as index
    df.set_index('date', inplace=True)
    
    # Resample to daily frequency and forward fill missing values
    df = df.resample('D').ffill()
    
    # Return NumPy array of values
    return df['value'].values
