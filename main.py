
from texto.obtener import WeatherInfo

from imagen.obtenerimg import ImageScraper

from Youtube.ObtenerList import search_youtube_music
def main():
    while True:
        print("Seleccione una opción:")
        print("1. Obtener información del clima")
        print("2. Descargar Imagenes")
        print("3. Busqueda en YouTube")
        choice = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

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

        if choice == '3':
            # Realizar la búsqueda de música en YouTube
            search_query = "música"
            search_youtube_music(search_query)

        else:
            print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
