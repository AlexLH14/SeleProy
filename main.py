'modulos a importa que deberian ser llamadas a el folder imagen o texto segun el usuario indique'


'que operacion quieres hacer 1 texto o 2 imagen y que si es cualquiera de los dos lo mando directamente a la clase del script '
' pertinente'

from texto.obtener import WeatherInfo

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Obtener información del clima")
        print("2. Descargar Imagenes")
        choice = input("Ingrese el número de la opción deseada (1 o 2): ")

        if choice == '1':
            weather = WeatherInfo()
            weather.get_weather_info()
            del weather
            break
        elif choice == '2':
           print("option")
        else:
            print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
