from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_classful import FlaskView



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chellasami54321#",
  database="inventory",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor() 


class InfoView(FlaskView):
  default_methods = ['GET', 'POST']
  def index(self):
        
    mycursor.execute("CREATE TABLE IF NOT EXISTS inventory.Info(Name varchar(50), Age int, Gender varchar(10), Salary float, Phno varchar(10), Dept varchar(50) )")
    
    mycursor.execute("SELECT * from inventory.Info")
    self.data = mycursor.fetchall()
    for row in mycursor:
        print (row)
    print (self.data)
    return render_template("info.html",value=self.data)

  def add(self):
    if request.method=='POST':
      Product.Name=request.form['Name']
      Product.Age=request.form['Age']
      Product.Gender=request.form['Gender']
      Product.Salary=request.form['Salary']
      Product.Phno=request.form['Phno']
      Product.Dept=request.form['Dept']

      sql = "INSERT INTO inventory.Info(Name,Age,Gender,Salary,Phno,Dept) VALUES (%s, %s,%s ,%s ,%s,%s)"
      val = (Product.Name,Product.Age, Product.Gender, Product.Salary, Product.Phno, Product.Dept)
      mycursor.execute(sql, val)
      mydb.commit()
      return redirect(url_for('InfoView:index'))
    return render_template("info_form.html")


class Cloths:
    pass
Product = Cloths()
