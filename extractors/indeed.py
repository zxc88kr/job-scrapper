from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_service = Service(executable_path=ChromeDriverManager().install())

def get_page_count(keyword):
    browser = webdriver.Chrome(options=chrome_options, service=chrome_service)
    base_url = "https://kr.indeed.com"
    browser.get(f"{base_url}/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label":"pagination"})
    pages = pagination.select("div a")
    count = len(pages) + 1
    for page in pages:
        if page["aria-label"] == "Previous Page":
            count -= 1
        if page["aria-label"] == "Next Page":
            count -= 1
    browser.quit()
    return count

def extract_indeed_jobs(keyword):
    results = []
    pages = get_page_count(keyword)
    browser = webdriver.Chrome(options=chrome_options, service=chrome_service)
    for page in range(pages):
        base_url = "https://kr.indeed.com"
        browser.get(f"{base_url}/jobs?q={keyword}&start={page * 10}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor.find("span").string
                company = job.find("span", class_="companyName").string
                location = job.find("div", class_="companyLocation").text.split("+")[0]
                link = anchor["href"]
                job_data = {
                    "position": title.replace(",", " "),
                    "company": company.replace(",", " "),
                    "location": location.replace(",", " "),
                    "link": f"{base_url}{link}"
                }
                results.append(job_data)
    browser.quit()    
    return results