from flask import Flask, render_template, request, session, redirect
import json
from sym import get_disease

app = Flask(__name__)
app.secret_key = "8d24209bf2b24de4b0571b35664d605b"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.db"

# db = SQLAlchemy(app)

# class USER(db.Model):
#     id = id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)

#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}')"

def add_user(user):
    with open("users.json", "r") as f:
        try:
            data = json.loads(f.read())
        except:
            data = dict()
    data[user['email']] = {"name" : user['name'], "password" : user['password']}
    with open("users.json", "w") as f:
        json.dump(data, f) 
        

def check(user):
    with open("users.json", "r") as f:
        try:
            data = json.loads(f.read())
        except:
            return False
    if user['email'] in data:
        return True
    else:
        return False

def login_user(user):
    with open("users.json", "r") as f:
        try:
            data = json.loads(f.read())
        except:
            return False
    if user['email'] in data:
        if data[user['email']]['password'] == user['password']:
            return True
    else:
        return False

@app.get("/")
def homepage():
    return render_template("home/home.html")

@app.get("/about")
def about_page():
    return render_template("about.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    try:
        if session['email'] != None:
            return redirect("/symptoms")
    except:
        pass
    if request.method == "POST":
        login_data = request.form
        exists = check(login_data)
        if exists:
            msg = login_user(login_data)
            if msg == True:
                session['email'] = login_data['email']
                return redirect("/symptoms")
            else:
                return redirect("/login")
        return redirect("/signup")
    
    return render_template("login.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    try:
        if session['email'] != None:
            return redirect("/symptoms")
    except:
        pass
    if request.method == "POST":
        signup_data = request.form
        exists = check(signup_data)
        if not exists:
            add_user(signup_data)
            session['email'] = signup_data['email']
            return redirect("/symptoms")
        else:
            return redirect("/login")
    return render_template("signup.html")

@app.route("/symptoms", methods = ['GET', 'POST'])
def symptoms():
    try:
        if session['email'] == None:
            return redirect("/login")
    except:
        pass
    if request.method == "POST":
        symptoms_data = request.form
        keys = symptoms_data.keys()
        symptoms = []
        for key in keys:
            values = symptoms_data[key].split(",")
            symptoms += values
        symptoms = ",".join(symptoms)
        disease = get_disease(symptoms)
        return disease
    return render_template("symptoms.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    # try:
    #     db.create_all()
    # except:
    #     pass
    app.run(debug=True)