# visualize_temperature.py

import matplotlib.pyplot as plt
from load_data import load_data
from constants import MONTHS

def visualize_average_temperature_2023():
    """Visualiza la temperatura media para cada mes del 2023 con subplots."""
    df = load_data()
    monthly_avg = df[df['year'] == 2023].groupby('month')[['max_temp', 'min_temp']].mean()

    # Visualización en un solo gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_avg.index, monthly_avg['max_temp'], label='Max Temp', color='red', marker='o')
    plt.plot(monthly_avg.index, monthly_avg['min_temp'], label='Min Temp', color='blue', marker='o')
    plt.title('Temperatura Media Diaria - 2023')
    plt.xticks(monthly_avg.index, MONTHS[:12], rotation=45)
    plt.xlabel('Mes')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Visualización usando subplots
    plt.figure(figsize=(14, 7))

    plt.subplot(1, 2, 1)
    plt.plot(monthly_avg.index, monthly_avg['max_temp'], color='red', label='Max Temp')
    plt.title('Temperatura Máxima - 2023')
    plt.xticks(monthly_avg.index, MONTHS[:12], rotation=45)
    plt.xlabel('Mes')
    plt.ylabel('Temperatura (°C)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(monthly_avg.index, monthly_avg['min_temp'], color='blue', label='Min Temp')
    plt.title('Temperatura Mínima - 2023')
    plt.xticks(monthly_avg.index, MONTHS[:12], rotation=45)
    plt.xlabel('Mes')
    plt.ylabel('Temperatura (°C)')
    plt.legend()

    plt.tight_layout()
    plt.show()
