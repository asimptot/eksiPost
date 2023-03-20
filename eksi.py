import sys
sys.path.append(r'C:\\Projects\\Eksi')
from init import *
from unidecode import unidecode

class Eksi:
    def setup(self):
        Setup.init(self)
        sleep(4)
        self.browser.get('https://eksisozluk.com/giris?returnUrl=https%3A%2F%2Feksisozluk.com%2F')
        sleep(4)

        actions = ActionChains(self.browser)
        M = 3
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        username = self.browser.find_element(By.ID, 'username')
        username.send_keys('YOUR EKSISOZLUK E-MAIL ADDRESS')

        password = self.browser.find_element(By.ID, 'password')
        password.send_keys('YOUR EKSISOZLUK PASSWORD')
        sleep(15)

        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-navigation"]/ul/li[6]/a'))
            )
            print('Logged in.')
        except:
            print('Failed to login.')
        sleep(10)

    def surf(self):
        self.browser.get('https://eksisozluk.com/basliklar/bugun')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/gundem')
        sleep(4)

        self.browser.get('https://eksisozluk.com/debe')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/sorunsal')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/takipentry')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/son')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kenar')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/caylaklar/bugun')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/spor')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/iliskiler')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/siyaset')
        sleep(4)

    def send_post(self):
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/a/span'))
        )
        main_title.click()
        sleep(4)

        get_url = self.browser.current_url
        sleep(4)

        self.browser.get(str(get_url)+'?p=3')
        sleep(4)

        copy = self.browser.find_element(By.XPATH, '//*[@id="entry-item"]/div[1]')
        copy = copy.text
        copy = unidecode(copy)
        sleep(4)

        paste = self.browser.find_element(By.XPATH, '//*[@id="editbox"]')
        paste.send_keys(copy)
        sleep(4)

        N = 2
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(4)

        if("efendimiz" in self.browser.page_source):
            print('Your post was sent successfully.')
        else:
            print('This entry already exists.')

    def fav(self):
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="entry-item"]/footer/div[1]/span[2]/a[1]'))
        )
        main_title.click()
        sleep(4)
        print('The post has been added to favorites.')

    def close_browser(self):
        Setup.close_browser(self)

eks = Eksi()
j = 0
while(True):
    i = 0
    eks.setup()
    try:
        while(True):
            try:
                eks.send_post()
                eks.surf()
                eks.fav()
                sleep(180)
                i = i + 1
            except:
                eks.close_browser()
        j = j + 1
    except:
        print('The topic title could not be found. Re-logging in...')
        eks.close_browser()
