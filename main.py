from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

keyword = input("What do you want to search for? ")

wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)
jobs = wwr + indeed

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()

'''
from requests import get
from bs4 import BeautifulSoup

def extract_jobs(term):
	results = []
	url = f"https://remoteok.com/remote-{term}-jobs"
	request = get(url, headers={"User-Agent": "Kimchi"})
	if request.status_code != 200:
		print("Can't get jobs.")
	else:
		soup = BeautifulSoup(request.text, "html.parser")
		jobs = soup.find_all("tr", class_="job")
		for job in jobs:
			title = job.find("h2", itemprop="title").string.strip()
			company = job.find("h3", itemprop="name").string.strip()
			location = job.find("div", class_="location").string.strip()
			link = job["data-href"]
			job_data = {
				"position": title,
				"company": company,
				"location": location,
				"link": f"https://remoteok.com{link}"
			}
			results.append(job_data)
	return results
	
jobs = extract_jobs("rust")
for job in jobs:
	print(job)
	print("/////\n/////")
'''