from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WeatherInfo:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_weather_info(self):
        self.driver.get("https://www.google.com")
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("Meteored")
        search_box.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
        links = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'meteored.mx')]")
        meteored_link = links[1]
        meteored_link.click()
        weather_info = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dato-temperatura"))).text
        print("Datos del clima en Chignahuapan:", weather_info)

    def __del__(self):
        self.driver.quit()

