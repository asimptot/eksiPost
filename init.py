from selenium import webdriver
from time import sleep
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.window import WindowTypes
import undetected_chromedriver as uc

class Setup:
    def init(self):
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        self.browser = uc.Chrome(options=options)

    def close_browser(self):
        self.browser.quit()
