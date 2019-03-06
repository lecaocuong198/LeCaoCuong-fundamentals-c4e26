from flask import Flask,render_template,request

app = Flask(__name__)
items = []

@app.route("/")
def menu():
    return 'Hello' + str(items)


@app.route("/add_bike",methods = ["GET","POST"])
def add_food():
    if request.method == "GET":
      return render_template("bike_form.html")
    elif request.method == "POST":
      form = request.form
      n = form['model']
      p = form['daily_fee']
      j = form['img_s']
      y = form['Year']
      new_item = {
        "model":n,
        "daily_fee":p,
        'image': j,
        'year': y,
      }
      items.append(new_item)
      s = f"model: {new_item['model']}\ndaily fee: { new_item['daily_fee']}\nimg_s:{new_item['image']}\nyear:{new_item['year']}"
      return  "Added\n"+s



if __name__ == '__main__':
  app.run(debug=True)