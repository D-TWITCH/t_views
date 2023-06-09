import os
import random
import multiprocessing
import time
from selenium import webdriver
#from chromedriver import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def your_function(url):

    options = Options()
    options.add_argument('--no_sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()


    urls = [os.getenv("URL"), os.getenv("URL2")]
    url = random.choice(urls)
    print(f'url: {len(url)}')
    driver.get(url)
    time.sleep(random.randint(5,10))

    #actions = ActionChains(driver)
    #actions.send_keys(Keys.SPACE)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_Selector, 'button[class="variant-action size-sm"]'))
        )
        driver.find_element(By.CSS_Selector, 'button[class="variant-action size-sm"]').clic()

    except:
        print("Not clicking")


    sleep_time = random.randint(30,300)
    print(f"Sleeping for: {sleep_time}")
    time.sleep(sleep_time)

    driver.quit()


if __name__ == '__main__':
    url = os.getenv("URL")
    users = os.getenv("USERS")
    arguments = []

    #for i in range(0, 7):
    for x in range(0, int(users)):
        arguments.append(url)

    pool = multiprocessing.Pool()
    pool.map(your_function, arguments)
    pool.close()
    pool.join()
