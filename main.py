# using flask_restful
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from utils.send_mail import send_mail


# creating the flask app
app = Flask(__name__)
CORS(app=app)


@app.route("/mail", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        result = send_mail(displayName=firstName+" "+lastName, mail=email, subject=subject, message=message)
        if result["payload"] is not None:
            return {"message": result["message"], "status": result["code"], "payload": result["payload"]}, result["code"]
        return {"message": "Mail Successfully Sent"}, 200


@app.route("/", methods=["GET"])
def new():
    if request.method == "GET":
        return "Server is working"


# driver function
if __name__ == '__main__':
    app.run(debug=True)
