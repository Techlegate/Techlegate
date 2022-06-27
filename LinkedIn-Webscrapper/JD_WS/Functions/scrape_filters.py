from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_site_remote(driver):
    site_types = []

    various_sites = driver.find_elements(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li")
    time.sleep(5)
    i = 1

    for jbtypes in various_sites:
        site_types.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[{i}]/label/p/span[1]").text)
        i += 1

    return site_types

def scrape_jobtypes(driver):
    job_types = []
    various_jobtypes = driver.find_elements(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[5]/fieldset/div/ul/li")
    time.sleep(5)
    i = 1

    for jbtypes in various_jobtypes:
        job_types.append((driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[5]/fieldset/div/ul/li[{i}]/label/p/span[1]")).text)
        i += 1

    return job_types

def scrape_times(driver):
    times = []
    various_times = driver.find_elements(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li")
    time.sleep(5)
    i = 1

    for tms in various_times:
        times.append((driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[{i}]/label/p/span[1]")).text)
        i += 1

    return times

def scrape_explvl(driver):
    exp_lvl = []
    various_exps = driver.find_elements(by = By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li")
    time.sleep(5)
    i = 1

    for exp in various_exps:
        exp_lvl.append((driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[{i}]/label/p/span[1]")).text)
        i += 1
    
    return exp_lvl

def scrape_filters(driver, exp_lvl_list, time_list, job_type_list, onsite_list, div_value):

    driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/section/div/div/div/div/div/button").click()

    exp_lvl_list = scrape_explvl(driver)
    print(f"Exp. Level: {exp_lvl_list}")
    time.sleep(5)

    time_list = scrape_times(driver)
    print(f"Job posted: {time_list}")
    time.sleep(5)

    job_type_list = scrape_jobtypes(driver)
    print(f"Job Type: {job_type_list}")
    time.sleep(5)

    onsite_list = scrape_site_remote(driver)
    print(f"On-Site/Remote: {onsite_list}")
    time.sleep(5)