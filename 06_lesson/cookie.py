from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


driver.get("https://www.labirint.ru/")

driver.add_cookie(cookie) #добавить куки
cookie = driver.get_cookie('PHPSESSID')
cookies = driver.get_cookies

#cookies = driver.get_cookies() #показать все куки
#print(cookies) #вывести в консоль


#driver.refresh()
driver.delete_all_cookies() #удалить все куки
#driver.refresh()


driver.quit()