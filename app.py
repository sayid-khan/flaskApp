from flask import Flask

app = Flask(__name__) #we are creating a object of Flask(as app) [becoz flask is a class]

#decorator for creating route
@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to the channel"

if __name__ == "__main__" :
    app.run(debug=True)