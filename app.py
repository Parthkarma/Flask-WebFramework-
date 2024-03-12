from flask import Flask ,render_template , request
#  here __name__ holds the name of the current module !
app = Flask(__name__) 
                         #  ROUTING : 
@app.route("/",methods=["GET"])
def welcome():
    return "<h1><b>Welcome to the flask app!<b><h1>"  #we can also use html tags !
@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the index page!"

@app.route("/main" ,methods = ["GET"] )
def main():
    return "Main page"

                        #Variable Rule 
@app.route('/success/<int:score>')  #variable will be written inside <> .
def success(score):
    return " <h1> i have scored :"+str(score) +"in exams. <h1>"
          #HTML page rendering and Redirection
@app.route('/form' , methods = ["GET" , "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
if __name__ == "__main__":
    app.run(debug=True)


                      
    


