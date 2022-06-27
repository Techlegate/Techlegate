from selenium.webdriver.common.by import By

def calc_jobs(driver, div_value):
    no_jobs = driver.find_element(by=By.XPATH, value=f'/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small').text
    print(f"Jobs present: {no_jobs}")