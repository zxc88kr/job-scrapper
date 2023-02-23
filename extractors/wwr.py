from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    results = []
    base_url = "https://weworkremotely.com"
    response = get(f"{base_url}/remote-jobs/search?term={keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)
            for post in job_posts:
                anchor = post.find_all("a")[1]
                title = anchor.find("span", class_="title").string
                company = anchor.find_all("span", class_="company")[0].string
                location = ""
                if len(anchor.find_all("span", class_="company")) == 3:
                    location = anchor.find_all("span", class_="company")[2].text
                link = anchor["href"]
                job_data = {
                    "position": title.replace(",", " "),
                    "company": company.replace(",", " "),
                    "location": location.replace(",", " "),
                    "link": f"{base_url}{link}"
                }
                results.append(job_data)
    return results