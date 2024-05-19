import time
from datetime import datetime

import allure
import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install()


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


def test_part1(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    input_field = driver.find_element(By.ID, "id_text_string")
    input_field.send_keys("IamAQA")
    input_field.send_keys(Keys.ENTER)
    print(driver.find_element(By.ID, "result-text").text)


def test_part2(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, "firstName").send_keys("Alice")
    driver.find_element(By.ID, "lastName").send_keys("Smith")
    driver.find_element(By.ID, "userEmail").send_keys("mail@inbox.ru")
    gender_field = driver.find_elements(
        By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline']")
    gender_field[0].click()
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    driver.find_element(By.ID, "subjectsInput").send_keys("Moscwo")
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("Moscow 13")
    button_submot = driver.find_element(By.XPATH, "//button[@id='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", button_submot)
    button_submot.click()

    for i in driver.find_elements(By.XPATH, "//tbody/tr"):
        print(i.text)
    time.sleep(10)


def test_part3_1(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_list = driver.find_element(By.ID, "id_choose_language")
    dropdown = Select(select_list)
    dropdown.select_by_visible_text("Python")
    driver.find_element(By.ID, "submit-id-submit").click()
    assert driver.find_element(By.ID, "result-text").text == "Python"


def test_part3_2(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.XPATH, "//button").click()
    assert driver.find_element(By.XPATH, "//h4[text()='Hello World!']")
