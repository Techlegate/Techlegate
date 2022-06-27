import time
from selenium.webdriver.common.by import By
from functions.gather_details import gather_education, gather_experience, gather_skills
from functions.to_csv import to_csv
from functions.start_linkedin import start_linkedin

def run(driver):
    driver.maximize_window()

    start_linkedin(driver)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

    candidate_name = driver.find_element(by = By.TAG_NAME, value="h1").text
    current_designation = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]").text
    current_location = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]").text
    candidate_about = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]").text
    education = gather_education(driver)
    skills = gather_skills(driver)
    experiences = gather_experience(driver)

    print(f"'Name': {candidate_name}\n'Designation': {current_designation}\n'Location': {current_location}\n'About the Candidate': {candidate_about}\n'Skills': {skills}\n'Education': {education}\n'Experiences': {experiences}")
    # to_csv({'Name': candidate_name, 'Designation': current_designation, 'Location': current_location, 'About the Candidate': candidate_about, 'Skills': skills, 'Education': education, 'Experiences': experiences})