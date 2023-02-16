# using flask_restful
from flask import Flask, jsonify, request, Response
from utils.send_mail import send_mail
from config.config import settings

# creating the flask app
app = Flask(__name__)

@app.route("/mail", methods=["GET","POST"])
def index():
	if request.method == "POST":
	    firstName = request.form["firstName"]
	    lastName = request.form["lastName"]
	    email = request.form["email"]
	    subject = request.form["subject"]
	    message = request.form["message"]
	    send_mail(firstName= firstName, lastName= lastName, email= email, subject= subject, message= message)
	    return Response(response="Contact Recieved", status=200)
	    
@app.route("/", methods=["GET"])
def new():
	if request.method == "GET":
	    return "Server is working"

# driver function
if __name__ == '__main__':
    app.run(debug = True)
