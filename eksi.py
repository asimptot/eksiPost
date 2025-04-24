import g4f.models
from g4f.Provider import RetryProvider
from init import *

provider_names = [
    "Chatgpt4o",
    "ChatgptFree",
    "Free2GPT",
    "GizAI",
    "Pizzagpt",
    "Qwen_QVQ_72B",
    "Qwen_Qwen_2_5",
    "Qwen_Qwen_2_5M",
    "Qwen_Qwen_2_5_Max",
    "Qwen_Qwen_2_72B"
]

providers = []
for name in provider_names:
    try:
        ProviderClass = getattr(g4f.Provider, name)
        providers.append(ProviderClass)
    except AttributeError:
        print(f"⚠️ Provider not found: {name}")

client = Client(provider=RetryProvider(providers, shuffle=False))

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
            password = self.browser.find_element(By.ID, 'password')
            password.send_keys('YOUR EKSISOZLUK PASSWORD')
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
            "__Secure-1PSID": "g.a000tQh7b-GAI3EITmLI48xlpHeCniEPrQiuyIDFUwOBvUgPmzFD3pBwILVZ7GOkQRvhgrqRmgACgYKATwSAQASFQHGX2MiqiwVSp7DMbLLkGCXRaiTzBoVAUF8yKoEZ8LYVHn5uIY4NPB8VO_50076"})

        prompt = (f"{title} ile ilgili gercek deneyimlerden ilham alinan, alt basliklari olmayan(** icermeyen) bir kisa bir yazi uret. Emoji "
                  f"kullanmamalisin, imla hatalari yapabilirsin ve devrik dil kullanabilirsin. Yazinin bir insan elinden "
                  f"ciktigina inandirmalisin. Futbolla ilgili paylasim yapma. Robot gibi konusma. Kisa yazilar yaz. "
                  f"Lutfen samimi sekilde gonderilerini paylas. Cinsiyetin erkek, yani kadin tepkileri verme ve kadinsi "
                  f"ifadeler kullanma. Asiri lakayt ve ciddiyetsiz biri gibi ol. Sadece gonderiyi uret, kendi yorumunu ekleme. "
                  f"** karakerleri arasina kelimeler getirip baslik ureme. Sadece gonderi olsun. ")
        response = client.chat.completions.create(
            model=g4f.models.gpt_4o,
            web_search = True,
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
