
from texto.obtener import WeatherInfo

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Obtener información del clima")
        choice = input("Ingrese el número de la opción deseada (1 o 2): ")

        if choice == '1':
            weather = WeatherInfo()
            weather.get_weather_info()
            del weather
            break

        else:
            print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
