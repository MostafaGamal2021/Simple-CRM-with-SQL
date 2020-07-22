from tkinter import *
import mysql.connector


root = Tk()
root.title('MGA')
root.geometry('400x200')
root.iconbitmap('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images/moon.ico')

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "professor2020",
                                )

print(mydb)

root.mainloop()