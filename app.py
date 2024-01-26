from flask import Flask, request, render_template

import google.generativeai as palm
palm.configure(api_key="AIzaSyDJ1gjXaT1ut5sYTBn5HaMQAGGaYXzSzAc")
model = {"model":"models/chat-bison-001"}


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])

def index():
    if request.method =="POST":
        q = request.form.get("q")
        print("q")
        r = palm.chat(
        **model,
        # ** pointer, can point to many parameters
        messages = q
        )
     
        return(render_template("Day9.html",result=r.last))
    else:
        return(render_template("Day9.html", result="waiting for question........."))
    
if __name__ =="__main__":
    app.run(port=5001)
