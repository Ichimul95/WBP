"""
Routes and views for the flask application.
"""

from datetime import datetime
import flask
from flask import render_template
from flask import request
from flask import redirect
from AccompaningProjects import app
import sqlite3


@app.route('/')
@app.route('/home')
def home():
  try:
   con = sqlite3.connect("secondTest.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from project")
   
   rows = cur.fetchall(); 
   return render_template("index.html",rows = rows)
  
  except Exception as ex:
   template = "An exception of type {0} occurred. Arguments:\n{1!r}"
   message = template.format(type(ex).__name__, ex.args)
   print(message) 

@app.route('/add')
def add():
     return render_template("add.html")


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
     if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         
         with sqlite3.connect("secondTest.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO project (temperature,humidity,datetime,checkbox)  VALUES (?,?,?,?)",(addr,city,datetime.now(),0) )
            
            con.commit()
            return render_template("index.html")
      except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message) 
      
   