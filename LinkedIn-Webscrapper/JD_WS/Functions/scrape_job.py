from selenium.webdriver.common.by import By

def scrape_details(driver, div_value):
    try:
        return (driver.find_element(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[2]/article/div/div[1]/span").text)
    except:
        return ('NA')

def scrape_apply(driver, div_value, i):
    try:
        return (driver.find_element(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a").get_attribute('href'))
    except:
        return ('NA')

def scrape_location(driver, div_value):
    try:
        return ((driver.find_element(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[2]")).text)
    except:
        return ('NA')

def scrape_position(driver, div_value):
    try:
        return (((driver.find_elements(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/a/h2"))[0]).text)
    except:
        return ('NA')

def scrape_companyname(driver, div_value):
    try:
        return ((driver.find_element(by = By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a")).text)
    except:
        return ('NA')

def scrape_job(driver, company_list, position_list, location_list, apply_list, details_list, div_value, i):
    position_list.append(scrape_position(driver, div_value))
    company_list.append(scrape_companyname(driver, div_value))
    location_list.append(scrape_location(driver, div_value))
    apply_list.append(scrape_apply(driver, div_value, i))
    details_list.append(scrape_details(driver, div_value))