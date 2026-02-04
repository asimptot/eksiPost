import g4f.models

from init import *
from config import EMAIL, PASSWORD, GOOGLE_SECURE_1PSID

provider_names = [
    "WeWordle",
    "Yqcloud",
    "OperaAria",
    "AnyProvider",
]

providers = []
for name in provider_names:
    try:
        ProviderClass = getattr(g4f.Provider, name)
        providers.append(ProviderClass)
    except AttributeError:
        print(f"Provider not found: {name}")

client = Client(provider=RetryProvider(providers, shuffle=True))

messages = []

class Eksi:
    def setup(self):
        Setup.init(self)
        while(True):
            try:
                sleep(4)
                break
            except:
                self.browser.refresh()
        sleep(2)

        actions = ActionChains(self.browser)
        M = 3
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

    def login(self):
        actions = ActionChains(self.browser)
        sleep(4)

        while True:
            try:
                M = 3
                for _ in range(M):
                    actions.send_keys(Keys.TAB).perform()
                actions.send_keys(Keys.SPACE).perform()
                sleep(2)

                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, 'username'))
                ).send_keys(EMAIL)
                break
            except:
                pass

        password = self.browser.find_element(By.ID, 'password')
        password.send_keys(PASSWORD)
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
            password = self.browser.find_element(By.ID, 'password')
            password.send_keys(PASSWORD)
            sleep(5)
            for _ in range(2):
                actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.SPACE).perform()
            sleep(10)
            for _ in range(5):
                actions.send_keys(Keys.TAB).perform()
            sleep(1)
            actions.send_keys(Keys.RETURN).perform()
            sleep(10)
            #Eksi.login(self)
            self.browser.save_screenshot('hata.png')
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
        try:
            title = self.browser.find_element(By.XPATH, '//*[@id="title"]').text
            #posts = self.browser.find_element(By.XPATH, '//*[@id="entry-item-list"]').text
        except:
            print('burada sorun var.')

        set_cookies(".google.com", {
            "__Secure-1PSID": GOOGLE_SECURE_1PSID})

        prompt = (f"{title} basligina Eksi Sozluk'e entry gireceksin. Tamamen gercek bir insan gibi yaz. "
                  f"ONEMLI: Kelimeleri vurgulamak icin ASLA ASLA yildiz (*) veya cift yildiz (**) kullanma! "
                  f"Sadece normal duz metin kullan. Hicbir kelimeyi * isaretleri arasina alma! "
                  f"Markdown formatlamasi yapma, bold yapma, italic yapma! "
                  f"Alt baslik yapma, madde islemi yapma! Sadece duz paragraf yaz. "
                  f"Harfleri NORMAL bitisik yaz, 's a m p i y o n' gibi aralikli yazma! "
                  f"Eksi Sozluk'teki gibi gundelik, dogal, samimi yaz. Imla hatasi yapabilirsin. "
                  f"'umit ederim begenirsin', 'yardimci olabilir miyim', 'hazirladim' gibi yapay zeka cikisi cumleler YAZMA! "
                  f"Bunlar yapay zeka ifadeleri, insan boyle yazmaz. "
                  f"Emoji kullanma. Erkek bir kullanici gibi yaz. Cok ciddi olma, rahat yaz. "
                  f"Futbol konularindan uzak dur. Kisa ve oz yaz, 3-5 cumle yeter. "
                  f"Sadece entry'i yaz, baska hicbir sey yazma!")
        response = client.chat.completions.create(
            model=g4f.models.gpt_4_5,
            web_search = False,
            messages=[{"role": "user", "content": prompt}],
        )

        generated_text = response.choices[0].message.content
        generated_text = generated_text.encode('utf-8').decode('utf-8')

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