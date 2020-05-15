from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Pool

KahootId = "611254"
Prefijo = "Bot Name"
NumeroDeBots = 10

def mainFunc(number):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://kahoot.it/")
    search = driver.find_element_by_id("game-input")
    search.send_keys(KahootId)
    search.send_keys(Keys.RETURN)

    try:
        nickname = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nickname"))
        )
        search = driver.find_element_by_id("nickname")
        search.send_keys(Prefijo + ": " + number)
        search.send_keys(Keys.RETURN)
    except:
        driver.close()


if __name__ == '__main__':
    args = []
    for i in range(1, NumeroDeBots + 1):
        args.append(str(i))
    bot = Pool()
    argStorage = args * 1
    bot.map(mainFunc, argStorage)
