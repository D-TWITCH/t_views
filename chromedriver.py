from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class ChromeDriver:

    def __init__(self):
        options = Options()
        options.add_argument('--no_sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("start-maximized")
        options.addArguments("disable-infobars")
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()
