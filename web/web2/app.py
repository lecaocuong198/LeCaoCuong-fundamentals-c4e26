from flask import Flask,render_template,request
#Jinja2
#a = ancher
app = Flask(__name__)
items = [
  {"name":"abcd",
  "price":250000,
  },
 {"name":"com",
  "price":35000,
  }, {"name":"pho",
  "price":45000,
  },
  {"name":"bun ca",
  "price":55000,
  }
]

@app.route("/")
def menu():
    return render_template("menu.html",item_list = items,)

@app.route("/food/<int:i>")
def food(i):
    return render_template("food_detail.html", item=items[i])

@app.route("/add_food",methods = ["GET","POST"])
def add_food():
    if request.method == "GET":
      return render_template("food_form.html")
    elif request.method == "POST":
      form = request.form
      n = form['name']
      p = form['price']
      new_item = {
        "name":n,
        "price":p,
      }
      items.append(new_item)
      return n +"added"



if __name__ == '__main__':
  app.run(debug=True)