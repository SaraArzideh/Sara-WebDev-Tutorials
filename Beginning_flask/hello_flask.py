from flask_test.hello_flask import Flask       # import flask class

app=Flask(__name__)           # create an object of flask class

@app.route("/")               # using rout decorator to tell Flask what URL should trigger our function.

def home():
    return "Hello Flask"

if __name__=="__main__":
    app.run("127.0.0.1", port=8080)
