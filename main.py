from flask import Flask, request, render_template, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.remote import extract_remote_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = { }

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword").strip()
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        remote = extract_remote_jobs(keyword)
        try:
            indeed = extract_indeed_jobs(keyword)
            jobs = wwr + remote + indeed
        except:
            jobs = wwr + remote
        db[keyword] = jobs
    count = len(jobs)
    return render_template("search.html", keyword=keyword, count=count, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword").strip()
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1")