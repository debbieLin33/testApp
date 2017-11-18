from flask import Flask, request, abort


app = Flask(__name__)



@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return data



if __name__ == "__main__":
    app.run()



