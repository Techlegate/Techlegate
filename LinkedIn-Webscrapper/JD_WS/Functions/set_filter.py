from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def set_time(driver, div_value, filter_value):
    try:
        driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[{filter_value[0]}]/label").click()
        time.sleep(10)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[3]/div/button[2]").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[1]/label").click()
        time.sleep(10)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[3]/div/button[2]").send_keys(Keys.ENTER)
        time.sleep(5)

def set_experience(driver, div_value, filter_value):
    driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()
    time.sleep(5)
    try:
        for _ in filter_value:
            driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[{_}]/label").click()
            time.sleep(10)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[3]/div/button[2]").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        pass

def set_jobtype(driver, div_value, filter_value):
    driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()
    time.sleep(5)
    try:
        for _ in filter_value:
            driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[5]/fieldset/div/ul/li[{_}]/label").click()
            time.sleep(10)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[3]/div/button[2]").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        pass

def set_site(driver, div_value, filter_value):
    driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()
    time.sleep(5)
    try:
        for _ in filter_value:
            driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[{_}]/label").click()
            time.sleep(10)
        driver.find_element(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[3]/div/button[2]").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        pass