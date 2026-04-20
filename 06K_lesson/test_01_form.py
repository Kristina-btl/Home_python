import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()

def test_form_submission_color_highlighting(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.NAME, "job-position").send_keys("QA")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_input = wait.until(EC.presence_of_element_located((By.NAME, "zip")))

    border_color = driver.execute_script("""
            // Возвращаем точный цвет границы
            return window.getComputedStyle(arguments[0]).borderColor;
        """, zip_input)
    assert border_color.strip() == "rgb(245, 194, 199)", "Поле ZIP Code подсвечено красным!"

# Проверяем остальные поля
    fields = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phoneNumber": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job": "QA",
            "company": "SkyPro"
        }

    for name, value in fields.items():
        elem = wait.until(EC.presence_of_element_located((By.NAME, name)))

    assert elem.get_attribute("value") == value, f"Поле {name} содержит неправильное значение"

    border_color = driver.execute_script("""
                return window.getComputedStyle(arguments[0]).borderColor;
            """, elem)

    assert border_color.strip() == "rgb(186, 219, 204)", f"Поле {name} подсвечено зелёным!"



    driver.quit()