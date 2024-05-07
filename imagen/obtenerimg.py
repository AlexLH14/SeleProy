import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ImageScraper:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def scrape_images(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
        for idx, image in enumerate(images):
            url_image = image.get_attribute('src')
            try:
                response = requests.get(url_image, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    image_name = f"imagen_{idx}.png"
                    image_path = os.path.join(self.folder_path, image_name)
                    with open(image_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Imagen {idx + 1} guardada en: {image_path}")
                else:
                    print(f"Error al descargar la imagen {idx + 1}: {response.status_code}")
            except Exception as e:
                print(f"Error al descargar la imagen {idx + 1}: {str(e)}")
        driver.quit()
