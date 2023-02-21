from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)
            for post in job_posts:
                anchor = post.find_all("a")[1]
                title = anchor.find("span", class_="title")
                company, kind, region = anchor.find_all("span", class_="company")
                link = anchor["href"]
                job_data = {
                    "position": title.string.replace(",", " "),
                    "company": company.string.replace(",", " "),
                    "location": region.string.replace(",", " "),
                    "link": f"https://weworkremotely.com{link}"
                }
                results.append(job_data)
        return results