from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import time
import os

URL = "https://www.jio.com/help/faq/jiofiber/jioairfiber/aboutproduct#/"
FILE = "jio_scraper/articles.txt"

class Scraper:
    def __init__(self):
        self.driver = self.create_driver()
    
    def create_driver(self):
        chrome_options = Options()
        load_dotenv()
        user_data_dir = os.getenv("USER_DATA_DIR")
        chrome_options.add_argument(user_data_dir)
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    
    def scrape(self, url):
        self.driver.get(url)
        articles = []

        links = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(By.XPATH, "//*[@id=\"SecondList\"]/div/div/div/ul/li/a")
        )

        for i in range(len(links)):
            self.driver.execute_script("arguments[0].click();", links[i])
            links = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_elements(By.XPATH, "//*[@id=\"SecondList\"]/div/div/div/ul/li/a")
            )
            question_bottons = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_elements(By.XPATH, "/html/body/div[3]/section[2]/div/div[3]/div[2]/section/div/div/div/div/div/div/button/div/div/div[2]/span")
            )
            for i in range(len(question_bottons)):
                self.driver.execute_script("arguments[0].click();", question_bottons[i])
                article = WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element(By.XPATH, f"/html/body/div[3]/section[2]/div/div[3]/div[2]/section/div/div/div/div/div/div[{i+1}]")
                )
                articles.append(article.text)

        with open(FILE, "w+", encoding="utf-8") as file:
            for i, article in enumerate(articles):
                file.write(f"{i + 1}. {article}\n\n")
        
        return None
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape(URL)
    scraper.close()