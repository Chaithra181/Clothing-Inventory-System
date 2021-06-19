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

class OrderView(FlaskView):
  default_methods = ['GET', 'POST']
  def index(self):
        
    sql = "CREATE TABLE IF NOT EXISTS inventory.orders(order_id varchar(10),cust_id varchar(10),items varchar(10),quantity int,cost float)"
    mycursor.execute(sql)
    
    mycursor.execute("SELECT * from inventory.orders")
    self.data = mycursor.fetchall()
    for row in mycursor:
        print (row)
    print (self.data)
    return render_template("orders.html",value=self.data)

  def add(self):
    if request.method=='POST':
      Product.Order_Id=request.form['Order_Id']
      Product.Cust_Id=request.form['Cust_Id']
      Product.Items=request.form['Items']
      Product.Quantity=request.form['Quantity']
      Product.Price=request.form['Cost']

      

      sql = "INSERT INTO inventory.orders(order_id,cust_id,items,quantity,cost) VALUES (%s, %s,%s ,%s ,%s)"
      val = (Product.Order_Id, Product.Cust_Id, Product.Items, Product.Quantity, Product.Price)
      mycursor.execute(sql, val)
      mydb.commit()
      return redirect(url_for('OrderView:index'))
    return render_template("order_form.html")

  def remove(self):
    if request.method =='POST':
      Product.Order_Id=request.form['Order_Id']
      sql = "DELETE FROM inventory.orders WHERE order_id = %s"
      val = (Product.Order_Id,)
      mycursor.execute(sql,val)
      mydb.commit()
      return redirect(url_for('OrderView:index'))
    return render_template("orders_form_remove.html")

class Cloths:
  pass
Product = Cloths()
