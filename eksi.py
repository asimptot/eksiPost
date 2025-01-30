from init import *
from unidecode import unidecode

warnings.filterwarnings("ignore")
client = Client()
messages = []

class Eksi:
    def setup(self):
        Setup.init(self)
        while(True):
            try:
                sleep(10)
                break
            except:
                self.browser.refresh()
        sleep(4)

        actions = ActionChains(self.browser)
        M = 3
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

    def login(self):
        actions = ActionChains(self.browser)
        #self.browser.get('https://eksisozluk.com/giris')
        sleep(4)

        while True:
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, 'username'))
                ).send_keys('YOUR EKSISOZLUK USERNAME')
                break
            except:
                pass

        password = self.browser.find_element(By.ID, 'password')
        password.send_keys('YOUR EKSISOZLUK PASSWORD')
        sleep(5)

        actions.send_keys(Keys.RETURN).perform()
        sleep(5)
        self.browser.save_screenshot('login.png')

        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-navigation"]/ul/li[6]/a'))
            )
            print('Logged in.')
        except:
            print('Failed to login.')
            #Eksi.login(self)
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

        try:
            last = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="topic"]/div[1]/div[2]/a[1]'))
            )
            last.click()
        except:
            self.browser.refresh()
            main_title = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/a/span'))
            )
            main_title.click()
            sleep(4)
            last = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="topic"]/div[1]/div[2]/a[1]'))
            )
            last.click()
        sleep(4)
        all_context = self.browser.find_element(By.XPATH, '//*[@id="topic"]').text

        prompt = f"Bu metne dayanarak emoji kullanmadan havali bir içerik üret ve lutfen sadece urettigin icerigi paylas: {all_context}"
        response = client.chat.completions.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": prompt}],
        )

        generated_text = response.choices[0].message.content
        generated_text = unidecode(generated_text)

        paste = self.browser.find_element(By.XPATH, '//*[@id="editbox"]')
        paste.send_keys(generated_text)
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
            sleep(180)
        else:
            print('An error occurred while sending the post.')

    def fav(self):
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="entry-item"]/footer/div[1]/span[2]/a[1]'))
        )
        main_title.click()
        sleep(4)
        print('The post has been added to favorites.')

    def close_browser(self):
        Setup.close_browser(self)

eks = Eksi()
eks.setup()
eks.login()

while(True):
    try:
        eks.send_post()
        eks.surf()
        eks.fav()
    except:
        print('No content has been found to copy. Retrying...')
        eks.close_browser()
        eks.setup()
        try:
            eks.login()
        except:
            sleep(1)
