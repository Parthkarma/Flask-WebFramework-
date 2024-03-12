from flask import Flask
from flask import request       # for input 
app = Flask(__name__)

@app.route("/0")
def hello_world1():
    return "hello , World! 0 "
@app.route("/1")
def hello_world2():
    return "hello , World 1 !"
@app.route("/2")
def hello_world3():
    return "hello , World 2 !"
@app.route("/test_fun")      # not calling it by the name of the function  
def test():
    a = 5 + 6 
    return "this is my first function in flask {}".format(a)
#          For Input 
@app.route("/input_url")
def request_input():
    data = ('x') 
       # request an argument and get it from the url 
    return "This is my input from URL  : {}".format(data)
if __name__ == "__main__":
    app.run(host = "0.0.0.0")


