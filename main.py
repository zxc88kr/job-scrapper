from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.remote import extract_remote_jobs
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
        indeed = extract_indeed_jobs(keyword)
        remote = extract_remote_jobs(keyword)
        jobs = wwr + indeed + remote
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

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