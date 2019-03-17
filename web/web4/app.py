from flask import Flask,render_template,request
from db import food_collection
import food

app = Flask(__name__)

@app.route("/food_list")
def food_list():
    #get all food
    all_food = food.get({})

    #render : food + html

    #return
    return render_template("food_list.html",f_list = all_food)

@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return f["name"]

#find_user_by_name
@app.route("/find/user/<name>")
def find_by_username(name):
    f = food.find_by_username(name)
    return render_template("find_user.html",id = f["_id"], name = f["name"]) 


    
@app.route("/add_food", methods = ["GET","POST"])
def add_food():
    if request.methods == "GET":
        return render_template("food_form.html")
    elif request.methods == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        food.add_food(n,p)
if __name__ == '__main__':
    app.run(debug=True)

#short uid