from flask import Flask,redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "hello! "

User = {
    "huy" : {
        "name": "Nguyen Quang Huy",
        "age": 29,
    },
    "tuananh":{
        "name": "Huynh Tuan Anh",
        "age":22,
    }
}


@app.route("/user/<name>")
def user(name):
    if name in User:
        return str(User[name])
    else:
        return "User not found"


if __name__ == '__main__':
  app.run(debug=True)
