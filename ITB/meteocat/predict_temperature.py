# predict_temperature.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_data
from constants import MONTHS

def predict_temperature():
    """Predicción de temperaturas medias para 2024."""
    df = load_data()
    monthly_avg = df.groupby('month')[['max_temp', 'min_temp']].mean()
    
    # Predicción para 2024
    predicted_max = monthly_avg['max_temp'].values
    predicted_min = monthly_avg['min_temp'].values

    plt.figure(figsize=(10, 5))
    plt.bar(MONTHS, predicted_max, color='red', alpha=0.5, label='Predicted Max Temp')
    plt.bar(MONTHS, predicted_min, color='blue', alpha=0.5, label='Predicted Min Temp')
    plt.title('Predicted Average Temperatures for 2024')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

    # Histograma de la distribución de temperaturas
    temperature_values = np.random.normal(loc=predicted_max.mean(), scale=5, size=365)
    
    plt.figure(figsize=(10, 5))
    plt.hist(temperature_values, bins=20, color='green', alpha=0.7)
    plt.title('Distribución de Temperaturas para 2024')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.show()
