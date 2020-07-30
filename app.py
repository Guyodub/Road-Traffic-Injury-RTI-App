from flask import Flask, render_template, request ,flash, redirect,url_for,session,logging,request

from flask_sqlalchemy import SQLAlchemy
from send_email import send_mail

app = Flask(__name__)

#define our database

ENV = 'dev'

if ENV == 'dev':
    app.config['SECRET_KEY'] = '966a98e7b6fd851217f6f90db9f0e1da'
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Green$8054@localhost:5432/rti_project'
     

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
###create database objects
db  =  SQLAlchemy(app)

##create a model
class Feedback(db.Model):
    __tablename__ = 'injuries'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime(timezone=False))
    vehicles  = db.Column(db.String(200))
    n_people = db.Column(db.Integer)
    location= db.Column(db.String(200))
    severity =  db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    officer = db.Column(db.String(200))
    
    def __init__(self, time,vehicles, n_people, location, severity , latitude,longitude,officer):
        self.time = time
        self.vehicles = vehicles
        self.n_people = n_people
        self.location = location
        self.severity = severity 
        self.latitude = latitude
        self.longitude = longitude
        self.officer = officer



class user(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80))
     email = db.Column(db.String(120))
     password = db.Column(db.String(80))
     
     
     def __init__(self, username , email, password):
         self.username = username
         self.email= email
         self.password = password


@app.route("/")
def index():
    return render_template("home.html")
    
# @app.route('/')

# def index(): #define a methof called index
#     return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('index.html')
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/submit", methods=['POST']) #handling submit method in our index.html filr
def submit():
    if request.method == 'POST':
        time = request.form['time']
        vehicles = request.form['vtype']
        n_people = request.form['people']
        location = request.form['location']
        severity = request.form['rating']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        officer = request.form['officer']
        #print(Date, time, vtype, plate, location, rating, comments, latitude, longitude)
        #return render_template('success.html')
       
        # if location == '' or plate == '':
        #     return render_template('index.html', message='Please enter required fields')
        
        data = Feedback(time, vehicles, n_people, location, severity , latitude,longitude, officer)
        db.session.add(data)
        db.session.commit()
        send_mail(time,vehicles, n_people, location, severity , latitude,longitude,officer)
        return render_template('success.html')
        #return render_template('index.html', message='This is already reported')

if __name__ == '__main__':
    db.create_all()
    app.run()# call app