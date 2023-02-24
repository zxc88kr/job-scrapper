from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.remote import extract_remote_jobs
from file import save_to_file
from flask import Flask

app = Flask("JobScrapper")

app.run("0.0.0.0")

'''
keyword = input("What do you want to search for? ")

wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)
remote = extract_remote_jobs(keyword)
jobs = wwr + indeed + remote

save_to_file(keyword, jobs)
'''