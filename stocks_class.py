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

class StocksView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        
        sql = "CREATE TABLE IF NOT EXISTS inventory.Stocks(Prod_Id varchar(15),Prod_Name varchar(15),Category varchar(15), Colour varchar(15),Gender varchar(15),Quantity int)"
        mycursor.execute(sql)

        mycursor.execute("SELECT * from inventory.Stocks")
        self.data = mycursor.fetchall()
        for row in mycursor:
            print (row)
        print (self.data)
        return render_template("stocks.html",value=self.data)

    def add(self):
        if request.method=='POST':
            Product.Prod_Id=request.form['Prod_Id']
            Product.Prod_Name=request.form['Prod_Name']
            Product.Category=request.form['Category']
            Product.Colour=request.form['Colour']
            Product.Gender=request.form['Section']
            Product.Quantity=request.form['Quantity']
            Product.Material=request.form['Material']
            Product.Price=request.form['Price']

            sql = "INSERT INTO inventory.Stocks(Prod_Id,Prod_Name,Category, Colour,Gender,Quantity) VALUES (%s, %s,%s ,%s ,%s ,%s)"
            val = (Product.Prod_Id, Product.Prod_Name, Product.Category, Product.Colour, Product.Gender, Product.Quantity)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(url_for('StocksView:index'))
        return render_template("stock_form.html")
    
    def remove(self):
        if request.method =='POST':
            Product.Prod_Id=request.form['Prod_Id']
            sql = "DELETE FROM inventory.Stocks WHERE Prod_Id = %s"
            val = (Product.Prod_Id,)
            mycursor.execute(sql,val)
            mydb.commit()
            return redirect(url_for('StocksView:index'))
        return render_template("stocks_form_remove.html")


class Cloths:
    pass
Product = Cloths()
