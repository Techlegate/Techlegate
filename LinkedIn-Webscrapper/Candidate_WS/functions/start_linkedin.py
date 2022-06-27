import time
from selenium.webdriver.common.by import By

def start_linkedin(driver):
    driver.get("https://www.linkedin.com/")
    time.sleep(5)

    driver.find_element(by = By.XPATH, value="//input[@id='session_key']").send_keys(input("Enter Email ID: "))
    driver.find_element(by = By.XPATH, value="//input[@id='session_password']").send_keys(input("Enter password: "))
    driver.find_element(by = By.XPATH, value="/html/body/main/section[1]/div/div/form/button").click()
    time.sleep(5)

    driver.get("https://in.linkedin.com/in/ashneer")