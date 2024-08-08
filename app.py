from flask import Flask, render_template, jsonify

app = Flask(__name__) #we are creating a object of Flask(as app) [becoz flask is a class]

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru',
        'salary' : 'Rs. 100000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Bengaluru',
        'salary' : 'Rs. 900000'
    },
    {
        'id' : 3,
        'title' : 'Frontend Engineer',
        'location' : 'Remote',
    },
    {
        'id' : 4,
        'title' : 'Backend Engineer',
        'location' : 'San Fransisco, USA',
        'salary' : '$ 50000'
    }

]

#decorator for creating route
@app.route("/",methods=["GET"])
def welcome():
    return render_template('home.html', jobs= JOBS, company_name = 'Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__" :
    app.run(debug=True)