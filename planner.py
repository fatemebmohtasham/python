import sqlite3
from datetime import datetime
from tabulate import tabulate
conn=sqlite3.connect('mydata.db')
c=conn.cursor()
def init():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS planner(
                            category  text COLLATE NOCASE,
                            amount    real,
                            date      text
                            )''') 
def insert(category,amount):
    with conn:  
        date=str(datetime.now().strftime('%Y-%M-%D|%H-%M')) 
        c.execute('INSERT INTO planner VALUES(:category,:amount,:date)',{'category':category,'amount':amount,'date':date})
def update(category,amount):
    with conn:  
        c.execute('UPDATE  planner SET  amount=:amount  WHERE (category=:category)',{'category':category,'amount':amount})    
def remove(category):
    with conn:
        c.execute('DELETE FROM planner WHERE (category=:category)',{'category':category})
def show(category=None):
    if category:
        c.execute('SELECT * FROM planner WHERE category=:category',{'category':category})
        resalts=c.fetchall()
        c.execute('SELECT sum(amount) FROM planner WHERE category=:category',{'category':category})
        amounts=c.fetchone()
    else:    
        c.execute('SELECT * FROM planner')
        resalts=c.fetchall()
        c.execute('SELECT sum(amount) FROM planner')
        amounts=c.fetchone()
    return resalts ,amounts

