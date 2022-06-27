from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def click_job(driver, i, div_value):
    try:
        driver.find_element(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a").send_keys(Keys.ENTER)
    except:
        pass