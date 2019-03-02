from flask import Flask,redirect
app = Flask(__name__)

#Bind route to view function
@app.route("/") #route
def home(): #view function
    return "hello!" #Bat buoc phai return de tra loi client

@app.route("/myclass")
def myclass():
    return ("bla..bla..")

@app.route("/hi/<name>")
def hi(name):
    return "hi"+name

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)

menu1 = ['com','pho xao','bun cha']
@app.route("/menu")
def menu():

    return  str(menu1)

@app.route("/food/<int:a>")
def food(a):
    return (menu1[a])

if __name__ == '__main__':
  app.run(debug=True)