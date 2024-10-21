# predict_rain.py

import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_data

def predict_rain():
    """Predicción de lluvia para 2024 basada en datos históricos."""
    df = load_data()
    rain_data = df.groupby(['year', 'month'])['precipitation'].sum().reset_index()
    
    # Calcular días de lluvia
    rainy_days = df[df['precipitation'] > 0].groupby(['year', 'month']).size().reset_index(name='rainy_days')
    
    # Merge para obtener probabilidades de lluvia
    rain_prob = pd.merge(rain_data, rainy_days, on=['year', 'month'])
    total_days = df['day'].nunique()  # Total de días en los datos
    rain_prob['rain_probability'] = rain_prob['rainy_days'] / total_days

    plt.figure(figsize=(10, 5))
    plt.bar(rain_prob['month'], rain_prob['rain_probability'], color='blue', alpha=0.6)
    plt.title('Probabilidad de Lluvia para 2024')
    plt.xlabel('Mes')
    plt.ylabel('Probabilidad')
    plt.xticks(rain_prob['month'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()

    # Diagrama de sectores
    rain_counts = [rain_prob['rainy_days'].sum(), total_days - rain_prob['rainy_days'].sum()]
    plt.figure(figsize=(8, 8))
    plt.pie(rain_counts, labels=['Días Lluviosos', 'Días No Lluviosos'], autopct='%1.1f%%', startangle=140)
    plt.title('Proporción de Días Lluviosos y No Lluviosos en 2024')
    plt.axis('equal')
    plt.show()
