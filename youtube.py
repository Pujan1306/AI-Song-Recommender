from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class YouTubeSearch:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.youtube.com")

    def search(self, gemini_response):
        self.search_bar = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
        self.search_bar.send_keys(gemini_response)
        self.search_bar.send_keys(Keys.ENTER)

        sleep(2)
        self.video = self.driver.find_element(By.CSS_SELECTOR, 'a[id="video-title"]')
        self.video.click()

        try:
            self.skip_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="ytp-skip-ad-button"]')))
            self.skip_button.click()
        except:
            pass

