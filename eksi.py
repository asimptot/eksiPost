import g4f.models
import sys
import asyncio
import os

from init import *
from config import EMAIL, PASSWORD, GOOGLE_SECURE_1PSID

# Force headless mode for g4f providers via environment variable
os.environ['WEBDRIVER_HEADLESS'] = '1'
os.environ['G4F_HEADLESS'] = 'true'

# Suppress asyncio task exception warnings
def suppress_exception_handler(loop, context):
    if 'exception' in context:
        exception = context['exception']
        if isinstance(exception, ConnectionRefusedError):
            return  # Suppress ConnectionRefusedError from nodriver
    # Let other exceptions pass through
    loop.default_exception_handler(context)

asyncio.get_event_loop().set_exception_handler(suppress_exception_handler)

provider_names = [
    "CohereForAI_C4AI_Command",
    "GeminiPro",
    "Groq",
    "Qwen_Qwen_3",
    "OperaAria",
    "Yqcloud",
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

        prompt = (f"Konu: {title}\n\n"
                  f"Bu konu hakkinda Eksi Sozluk'e kisa bir entry yaz. "
                  f"Onemli kurallar:\n"
                  f"- BASLIK METNINI TEKRARLAMA, basligi alintilama.\n"
                  f"- Ansiklopedi maddesi gibi yazma! Genel bilgi verme, tanim yapma!\n"
                  f"- Kendi basından gecmis gibi ya da kendi gorusun gibi yaz. Kisisel bir anekdot veya samimi bir yorum olsun.\n"
                  f"- 'insanlar', 'bircok kisi', 'sektorunde' gibi genel ifadeler kullanma. 'ben', 'benim', 'bizim' gibi kisisel ifadeler kullan.\n"
                  f"- Yildiz (*), cift yildiz (**), markdown, emoji KULLANMA.\n"
                  f"- Alt baslik, madde isareti yapma. Duz paragraf yaz.\n"
                  f"- Gundelik, laubali, samimi yaz. Devrik cumleler kur. Imla hatasi yapabilirsin.\n"
                  f"- Yapay zeka gibi konusma. 'hazirladim', 'iste sana', 'umarim begenirsin' gibi seyler YAZMA.\n"
                  f"- Erkek bir kullanici gibi yaz. Rahat ol, ciddiyetsiz ol.\n"
                  f"- 2-4 cumle yeter, uzun yazma.\n"
                  f"- Sadece entry metnini yaz, baska hicbir sey ekleme.")
        response = client.chat.completions.create(
            model=g4f.models.grok_3_r1,
            web_search = False,
            messages=[{"role": "user", "content": prompt}],
        )

        generated_text = response.choices[0].message.content
        generated_text = generated_text.encode('utf-8').decode('utf-8')
        # Remove all asterisks (bold/italic markdown formatting)
        generated_text = generated_text.replace('*', '')
        # Remove lines that look like meta commentary (e.g. "...başlığına entry:", "işte sana...")
        lines = generated_text.strip().split('\n')
        cleaned_lines = []
        for line in lines:
            lower = line.strip().lower()
            if any(phrase in lower for phrase in ['entry:', 'başlığına', 'basligina', 'işte sana', 'iste sana', 'hazırladım', 'hazirladim', '---']):
                continue
            cleaned_lines.append(line)
        generated_text = '\n'.join(cleaned_lines).strip()

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
    except KeyboardInterrupt:
        print('\nProgram stopped by user.')
        eks.close_browser()
        break
    except Exception as e:
        print(f'Error occurred: {type(e).__name__}. Retrying...')
        try:
            eks.close_browser()
        except:
            pass
        sleep(2)
        eks.setup()
        try:
            eks.login()
        except Exception as login_error:
            print(f'Login error: {type(login_error).__name__}')
            sleep(1)