from flask import Flask,redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "hello!"
personal_inf = {
    'name': 'Cuong',
    'work': 'student',
    'school': 'hubt',
    'hobbies': 'game',
    'pet': 'dog',
}

@app.route("/about-me")
def about_me():
    return str(personal_inf)

@app.route("/school")
def school():
    return redirect("http://techkids.vn") 

if __name__ == '__main__':
  app.run(debug=True)
