from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__) #we are creating a object of Flask(as app) [becoz flask is a class]
 
  

#decorator for creating route
@app.route("/",methods=["GET"])
def welcome():
    jobs_list = load_jobs_from_db()
    return render_template('home.html', jobs = jobs_list)


@app.route("/api/jobs")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)


@app.route("/job/<id>")   #<id> ->dynamic route
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found"
    return render_template('jobpage.html',job = job)


if __name__ == "__main__" :
    app.run(debug=True)