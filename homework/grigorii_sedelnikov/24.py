from datetime import datetime

import allure
import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_autoinstaller.install()


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(20)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


def test_ex_1(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com/index.html")
    item = driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    name_item = wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='name']"))).text
    driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
    wait.until(ec.alert_is_present()).dismiss()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[text()='Cart']"))).click()
    assert name_item == driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']").text


def test_ex_2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    item_card = driver.find_elements(By.XPATH, "//li[@class='item product product-item']")
    actions = ActionChains(driver)
    actions.move_to_element(item_card[0]).perform()
    driver.find_element(By.XPATH, "//span[text()='Add to Cart']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='counter-number']")))
    assert driver.find_element(By.XPATH, "//span[@class='counter-number']").text == "1"
