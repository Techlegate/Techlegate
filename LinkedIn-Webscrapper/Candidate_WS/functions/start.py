from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def start():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    return (webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=None))