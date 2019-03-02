from flask import Flask,redirect
import BMI
app = Flask(__name__)

@app.route("/")
def home():
    return "hello! Please enter your weight and height "

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    result = BMI.BMI(weight,height)
    return str(result)


if __name__ == '__main__':
  app.run(debug=True)
