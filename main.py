import sqlite3
#import mysql.connector
import tkinter as tk
from tkinter import *
import datetime
import threading
import time
import logging
from tkinter import ttk

try:
   print("sqlite open successfully")
   conn = sqlite3.connect('LoginUser.db')
except:
  print("An exception occurred")

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #password="",
  #database="posjavafx"
#)

def firstOption():
    
    root = tk.Tk()
    Program1  = tk.Frame(root)
    Program1.pack()
    tk.Label(Program1, text="Username").pack()

    # TextBox Creation
    inputtxt = tk.Text(Program1,
                   height = 5,
                   width = 20)

    inputtxt.pack()

    myCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)

    myCanvas.pack()

    
  

    print("Hello World")


def secondOption():
    print("Hello World2")


def thirdOption():
    print("Hello World3")



def openNewWindow():
     # creates a Tk() object



    MainProgram = tk.Tk()
    
    # sets the title of the
    # Toplevel widget
    MainProgram.title("New Window")
 
    # sets the geometry of toplevel
    MainProgram.geometry("200x200")
 
    # A Label widget to show in toplevel
    
    x = datetime.datetime.now()
    print(x)
    Label( MainProgram,
          text =x).pack()

    
    A = tk.Button(MainProgram, text ="Start new taking off", command = firstOption)
    A.pack()

       
    B = tk.Button(MainProgram, text ="Continue Saved File", command = secondOption)
    B.pack()
    
       
    C = tk.Button(MainProgram, text ="Example of Work", command = thirdOption)
    C.pack()

    D = tk.Button(MainProgram, text ="Exit", command = quit)
    D.pack()
   

def sql_login():
    #mycursor.execute("SELECT * FROM `products`")
    #print(mycursor.fetchall())
    login = "false"
    conn = sqlite3.connect('LoginUser.db')
    cur = conn.cursor()
    inp = inputtxt.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    #Get Username & Password
    cur.execute("SELECT * FROM User where Username = '" + inp +"'AND Password = '" +inp2 +"';")
    #Validation
    rows = cur.fetchall()
    
    if(rows == "[]"):
        print(rows)
        print("Password Error")
    else:
        print("Login")    
        frame.destroy() 
        openNewWindow()
      

    
    #for row in rows:
        #print(row)
        

    #inp = inputtxt.get(1.0, "end-1c")
    #print(inp)

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    print(inp)
    inp2 = inputtxt2.get(1.0, "end-1c")
    print(inp2)
    

def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Username").pack()

# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()

tk.Label(frame, text="Password").pack()
inputtxt2 = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt2.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="SQL",
                   command=sql_login)
slogan.pack(side=tk.LEFT)
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
# Label Creation
#lbl = tk.Label(frame, text = "")
#lbl.pack()
root.mainloop()