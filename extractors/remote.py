from requests import get
from bs4 import BeautifulSoup

def extract_remote_jobs(keyword):
    results = []
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = get(url, headers={"User-Agent": "Kimchi"})
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            title = job.find("h2", itemprop="title").string
            company = job.find("h3", itemprop="name").string
            location = job.find("div", class_="location").string
            while not location[0].isalpha():
                location = location[1:]
            link = job["data-href"]
            job_data = {
                "position": title.strip(),
                "company": company.strip(),
                "location": location.strip(),
                "link": f"https://remoteok.com{link}"
            }
            results.append(job_data)
    return results