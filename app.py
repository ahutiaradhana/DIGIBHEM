from flask import Flask, render_template, request
from sqlalchemy import SQLAlchemy
from phpmyadmin import phpmyadmiin

app = Flask(__name__)
app.config['phpmyadmin_DATABASE_URI'] = 'mysql://root:Miss@huti78539@localhost/expensetracker1'
db = phpmyadmiin(app)

#HOME--PAGE
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

#signup
class signup(db.model):
    Name =db.column(db.Varchar(100), primary_key = True)
    Email =db.column(db.Varchar(50), primary_key = False)
    Password =db.column(db.Varchar(20), primary_key = False)

@app.route("/signup",methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        Name = request.form.get('Name')
        Email = request.form.get('Email')
        Password = request.form.get('Password')

        entry = signup(Name=Name, Email=Email, PAssword=Password)
        db.session.add(entry)
        db.sesssion.commit()
        return render_template("signup.html")  

#LOGIN--PAGE  
class login(db.model):
    Username =db.column(db.Varchar(100), primary_key = True)
    Password =db.column(db.Varchar(20), primary_key = False)
@app.route("/login",methods=['GET','POST'])
def login():
    if(request.method=='POST'):
        Username = request.form.get('Userame')
        Password = request.form.get('Password')

        entry = signup(Username=Username, PAssword=Password)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("login.html")  

#ADDING----DATA
class add(db.model):
    date =db.column(db.int(), primary_key = True)
    expensename =db.column(db.varchar(100), primary_key = True)
    expenseamount=db.column(db.int(), primary_key = True)
@app.route("/add",methods=['GET','POST'])
def add():
    if(request.method=='POST'):
        date = request.form.get('date')
        expensename = request.form.get('expensename')
        expenseamount = request.form.get('expenseamount')
        entry = signup(date=date, expensename=expensename, expenseamount=expenseamount)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("add.html")

#delete---the--data
@app.route("/delete", methods = ['POST', 'GET' ])
def delete():
     print('deleted successfully')    
     return render_template("delete")


#UPDATE---DATA
class edit(db.model):
    date =db.column(db.int(), primary_key = True)
    expensename =db.column(db.varchar(100), primary_key = True)
    expenseamount=db.column(db.int(), primary_key = True)
@app.route("/add",methods=['GET','POST'])
def edit():
    if(request.method=='POST'):
        date = request.form.get('date')
        expensename = request.form.get('expensename')
        expenseamount = request.form.get('expenseamount')
        entry = signup(date=date, expensename=expensename, expenseamount=expenseamount)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("edit.html")

#limit
@app.route("/limit", methods = ['POST', 'GET' ])
def limit():
     print('limit entered successfully')    
     return render_template("limit.html")

#REPORT
class today(db.model):
    time =db.column(db.int(), primary_key = True)
    amount =db.column(db.int(100), primary_key = True)
    expensename =db.column(db.varchar(100), primary_key = True)
    expenseamount=db.column(db.int(), primary_key = True)
@app.route("/today",methods=['GET','POST'])
def today():
    if(request.method=='POST'):
        time = request.form.get('time')
        amount = request.form.get('amount')
        expensename = request.form.get('expensename')
        expenseamount = request.form.get('expenseamount')
        entry = signup(time= time, amount = amount, expensename=expensename, expenseamount=expenseamount)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("today.html")

class month(db.model):
    time =db.column(db.int(), primary_key = True)
    amount =db.column(db.int(100), primary_key = True)
    expensename =db.column(db.varchar(100), primary_key = True)
    expenseamount=db.column(db.int(), primary_key = True)
@app.route("/month",methods=['GET','POST'])
def today():
    if(request.method=='POST'):
        time = request.form.get('time')
        amount = request.form.get('amount')
        expensename = request.form.get('expensename')
        expenseamount = request.form.get('expenseamount')
        entry = signup(time= time, amount = amount, expensename=expensename, expenseamount=expenseamount)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("month.html")

class year(db.model):
    time =db.column(db.int(), primary_key = True)
    amount =db.column(db.int(100), primary_key = True)
    expensename =db.column(db.varchar(100), primary_key = True)
    expenseamount=db.column(db.int(), primary_key = True)
@app.route("/year",methods=['GET','POST'])
def today():
    if(request.method=='POST'):
        time = request.form.get('time')
        amount = request.form.get('amount')
        expensename = request.form.get('expensename')
        expenseamount = request.form.get('expenseamount')
        entry = signup(time= time, amount = amount, expensename=expensename, expenseamount=expenseamount)
        db.session.add(entry)
        db.sesssion.commit()
    return render_template("year.html")

#log-out
@app.route('/logout')

def logout():
   return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
