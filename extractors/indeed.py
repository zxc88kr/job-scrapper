from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(options=chrome_options, service=chrome_service)

browser.get("https://kr.indeed.com/jobs?q=python")

while (True):
    pass