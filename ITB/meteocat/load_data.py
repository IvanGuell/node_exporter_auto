# src/load_data.py

import pandas as pd
from constants import DATA_FILE_PATH

def load_data():
    """Load the weather data from a txt file into a DataFrame."""
    
    # Read the data
    df = pd.read_csv(DATA_FILE_PATH, sep='\s+', skiprows=16, encoding='ISO-8859-1')  # Cambiado delim_whitespace a sep='\s+'

    # Data cleaning
    df.columns = ['year', 'month', 'day', 'precipitation', 'max_temp', 'min_temp', 'insolation']
    df.dropna(inplace=True)
    
    # Convert to correct data types
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df['day'] = df['day'].astype(int)
    df['precipitation'] = df['precipitation'].astype(float)
    df['max_temp'] = df['max_temp'].astype(float)
    df['min_temp'] = df['min_temp'].astype(float)

    return df
