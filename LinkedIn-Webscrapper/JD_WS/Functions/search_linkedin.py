import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_linkedin(driver):
    driver.get("https://www.linkedin.com/jobs/search/")
    time.sleep(5)

    try:
        driver.find_element(by = By.XPATH, value="/html/body/div[6]/header/div/div/div/div[2]/div[1]/div/div/input[1]").send_keys("Accounts")
        driver.find_element(by = By.XPATH, value="/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]").clear()
        driver.find_element(by = By.XPATH, value="/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]").send_keys("Delhi")
        driver.find_element(by = By.XPATH, value="/html/body/div[6]/header/div/div/div/div[2]/button[1]").click()
        div = 6
    except:
        driver.find_element(by = By.XPATH, value="/html/body/div[5]/header/div/div/div/div[2]/div[1]/div/div/input[1]").send_keys("Accounts")
        driver.find_element(by = By.XPATH, value="/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]").clear()
        driver.find_element(by = By.XPATH, value="/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]").send_keys("Delhi")
        driver.find_element(by = By.XPATH, value="/html/body/div[5]/header/div/div/div/div[2]/button[1]").click()
        div = 5
    
    time.sleep(5)

    return div

# input("Search by title, skill or company: ")
# input("Enter city, state or zip code: ")