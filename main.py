

from texto.obtener import WeatherInfo

from imagen.obtenerimg import ImageScraper

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

        if choice == '2':
            # Crea una instancia de ImageScraper con la ruta donde guardarás las imágenes
            scraper = ImageScraper(r'C:\Users\alex2\Pictures\automatizacion')

            # Llama al método scrape_images con la URL del sitio web de donde deseas obtener las imágenes
            scraper.scrape_images("https://www.mediotiempo.com/futbol/liga-mx")
            
        else:
            print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
