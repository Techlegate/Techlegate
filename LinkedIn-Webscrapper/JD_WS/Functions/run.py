import imp
import time
from selenium.webdriver.common.by import By
from Functions.search_linkedin import search_linkedin
from Functions.set_filter import set_time, set_experience, set_jobtype, set_site
from Functions.scrape_filters import scrape_filters
from Functions.scrape_job import scrape_job
from Functions.calc_jobs import calc_jobs
from Functions.click_jobs import click_job
from Functions.login_linkedin import login_linkedin
from Functions.to_csv import to_csv

def run(driver):
    # Initializing all lists required to store details of jobs and filters
    company_list = []
    position_list = []
    location_list = []
    details_list = []
    apply_list = []
    exp_lvl_list = []
    time_list = []
    job_type_list = []
    onsite_list = []

    # Maximizing window size
    driver.maximize_window()

    # Login to LinkedIn using EmailID and Password
    login_linkedin(driver)
    time.sleep(5)

    # Search job on LinkedIn using Job Position or Location or Both
    div_value = search_linkedin(driver)
    time.sleep(5)

    # Filter to set the Date Posted
    set_time(driver, div_value, [4])

    # Filter to set the Experience Level
    # set_experience(driver, div_value, [6])

    # Filter to set the Job Type
    # set_jobtype(driver, div_value, [7])

    # Filter to set the Site
    # set_site(driver, div_value, [3])
    time.sleep(5)

    # Scraping filters
    scrape_filters(driver, exp_lvl_list, time_list, job_type_list, onsite_list, div_value)

    # Getting URL after applying filters and entering job search
    current_url = driver.current_url

    # Getting no. of jobs found
    calc_jobs(driver, div_value)
    try:
        no_pages = driver.find_elements(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li")
        pages = driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[{len(no_pages)}]/button/span").text
    except:
        pages = 1
    print(f"No. of pages: {pages}")
    time.sleep(60)

    page_no = 1
    k = 1

    # Looping through 100 jobs to scrape details
    for _ in range(25*int(pages)):

        if _ % 25 == 0:
            try:
                driver.find_element(by=By.XPATH, value=f"/html/body/div[{div_value}]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[{page_no}]/button").click()
            except:
                pass
            page_no += 1
            i = 1

        click_job(driver, i, div_value)
        time.sleep(5)

        print(f"Scraping job {k}")

        scrape_job(driver, company_list, position_list, location_list, apply_list, details_list, div_value, i)
        time.sleep(5)

        k += 1
        i += 1
    
    # Exporting to CSV sheet the details of job
    to_csv({"Company Name": company_list, "Position": position_list, "Location": location_list, "Apply Link": apply_list, "Details": details_list})