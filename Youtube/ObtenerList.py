from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def search_youtube_music(query):
    # Iniciar el navegador Chrome automáticamente
    driver = webdriver.Chrome()

    # Abrir la página de YouTube
    driver.get("https://www.youtube.com/")

    # Encontrar el campo de búsqueda y escribir la consulta
    search_box = driver.find_element(By.CSS_SELECTOR, "input#search")
    search_box.send_keys(query)

    # Presionar Enter para realizar la búsqueda
    search_box.send_keys(Keys.RETURN)

    # Esperar un momento para que se carguen los resultados
    time.sleep(5)

    # Encontrar los elementos que contienen los nombres de los videos
    video_elements = driver.find_elements(By.ID, "video-title")

    # Imprimir los nombres de los primeros 10 videos
    print("Los primeros 10 videos de la búsqueda son:")
    for i, video_element in enumerate(video_elements[:10]):
        print(f"{i + 1}. {video_element.text}")

    # Cerrar el navegador al finalizar
    driver.quit()


