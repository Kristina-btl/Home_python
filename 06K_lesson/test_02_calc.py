import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    wait = WebDriverWait(driver, 60)  

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear ()
    delay_input.send_keys ("45") 

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()


    result_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "screen")))

    result_text = result_element.text
    assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    

    driver.quit()