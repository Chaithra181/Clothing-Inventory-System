from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_classful import FlaskView

from orders_class import OrderView
from products_class import ProductView
from stocks_class import StocksView
from info_class import InfoView

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chellasami54321#",
  database="inventory",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor() 

app = Flask(__name__)

class HomeView(FlaskView):
  default_methods = ['GET','POST']
  route_base='/'

  mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory")

  def index(self):
    return redirect(url_for('HomeView:login'))

  def homepage_emp(self):
    return render_template("home1.html")  

  def homepage_man(self):
    return render_template("home2.html")  
  
  def login(self):
    access ={
      'employee':'pass',
      'manager':'pass'}
    error = None
    if request.method == 'POST':
      username = request.form['username']
      passwd = request.form['password']
      if username not in  access.keys() or passwd != access[username]:
        error = 'Invalid Credentials. Please try again.'
      else:
          if(username=='employee'):
            return redirect(url_for('HomeView:homepage_emp'))
          else:
            return redirect(url_for('HomeView:homepage_man'))
    return render_template('login.html', error=error)





HomeView.register(app)
StocksView.register(app)
OrderView.register(app)
ProductView.register(app)
InfoView.register(app)

if __name__ == '__main__':
  app.run(debug=True)
  
