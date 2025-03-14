from selenium import webdriver
from time import sleep
import warnings, ctypes
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.window import WindowTypes
import undetected_chromedriver as uc
import subprocess, g4f, warnings
from g4f.client import Client
from g4f.cookies import set_cookies

class Setup:
    def init(self):
        ctypes.windll.kernel32.SetThreadExecutionState(
            ctypes.c_uint(0x80000002)
        )
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-position=-2400,-2400")
        my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        options.add_argument(f"--user-agent={my_user_agent}")
        self.browser = uc.Chrome(options=options, version_main=133)
        self.actions = ActionChains(self.browser)
        self.browser.execute_script('''window.open("https://eksisozluk.com/giris","_blank");''')
        sleep(10)
        self.browser.switch_to.window(window_name=self.browser.window_handles[0])
        self.browser.close()
        self.browser.switch_to.window(window_name=self.browser.window_handles[0])
        sleep(2)

    def close_browser(self):
        self.browser.quit()
