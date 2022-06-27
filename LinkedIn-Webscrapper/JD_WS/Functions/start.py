from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Creating webdriver in headless mode
def start():
    options = Options()
    options.headless = True
    return (webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = None))