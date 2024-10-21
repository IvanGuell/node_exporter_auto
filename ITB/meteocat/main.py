# main.py

from visualize_temperature import visualize_average_temperature_2023
from predict_temperature import predict_temperature
from predict_rain import predict_rain

def main():
    """Función principal."""
    # Visualizar temperatura media de 2023
    visualize_average_temperature_2023()

    # Predicción de temperatura para 2024
    predict_temperature()

    # Predicción de lluvia para 2024
    predict_rain()

if __name__ == "__main__":
    main()
