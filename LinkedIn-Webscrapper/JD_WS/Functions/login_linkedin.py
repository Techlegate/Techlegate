import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login_linkedin(driver):
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    time.sleep(5)

    driver.find_element(by = By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[1]/input").send_keys("crypto.shinigami.leo@proton.me")
    driver.find_element(by = By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[2]/input").send_keys("ShinigamiLeo3000@")
    driver.find_element(by = By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").send_keys(Keys.ENTER)
    time.sleep(5)

# input("Enter email or phone number: ")
# input("Enter password: ")