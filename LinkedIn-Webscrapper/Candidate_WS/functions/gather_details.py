import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def gather_skills(driver):
    skill_list = []
    i = 1

    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[7]/div[3]/div/div/a").send_keys(Keys.ENTER)
        time.sleep(5)
        skills = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul/li")

        for skill in skills:
            skill_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/div/div[2]/div[1]/div[1]/div/span/span[1]").text)
            i += 1
    except:
        driver.get("https://in.linkedin.com/in/ashneer")
        time.sleep(5)

        skills = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[7]/div[3]/ul/li")

        for skill in skills:
            skill_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[7]/div[3]/ul/li[{i}]/div/div[2]/div[1]/div[1]/div/span/span[1]").text)
            i += 1
    
    driver.get("https://in.linkedin.com/in/ashneer")
    time.sleep(5)
    return(skill_list)

def gather_experience(driver):
    experience_list = []
    i = 1

    try:
        print("Click1")
        driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/div/div/a").send_keys(Keys.ENTER)
        time.sleep(5)
        print("Click1")
        experiences = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li")

        for exp in experiences:
            print("Click1")
            try:
                exp_list = []
                exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div/div[1]/div/span/span[1]").text)
                exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div/div[1]/span[1]/span[1]").text)
                exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div/div[1]/span[2]/span[1]").text)
            except:
                exp_list = []
                positions = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[2]/div/div[2]/div[2]/ul/li/div/div/div[1]/ul/li[1]")
                j = 1

                for pos in positions:
                    exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div[2]/ul/li/div/div/div[1]/ul/li[{j}]/div/div[2]/div/a/div/span/span[1]").text)
                    j += 1

                exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div[1]/a/div/span/span[1]").text)
                exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div/div[1]/ul/li[{i}]/div/div[2]/div[1]/a/span/span[1]").text)
            i += 1

            experience_list.append(exp_list)
    except:
        print("Click2")
        driver.get("https://in.linkedin.com/in/ashneer")
        time.sleep(5)
        print("Click2")
        experiences = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[7]/div[3]/ul/li")

        for exp in experiences:
            print("Click2")
            exp_list = []
            exp_list.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/div/div[2]/div[1]/div[1]/div/span/span[1]").text)
            i += 1
    print("Click3")
    driver.get("https://in.linkedin.com/in/ashneer")
    time.sleep(5)
    print("Click3")
    return(experience_list)

def gather_education(driver):
    i = 1
    degree_details = []

    qualifications = driver.find_elements(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[6]/div[3]/ul/li")

    for edu in qualifications:
        details = []
        details.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[6]/div[3]/ul/li[{i}]/div/div[2]/div[1]/a/div/span/span[1]").text)
        details.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[6]/div[3]/ul/li[{i}]/div/div[2]/div[1]/a/span[1]/span[1]").text)
        details.append(driver.find_element(by=By.XPATH, value=f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[6]/div[3]/ul/li[{i}]/div/div[2]/div[1]/a/span[2]/span[1]").text)
        degree_details.append(details)
        i += 1
    
    return(degree_details)