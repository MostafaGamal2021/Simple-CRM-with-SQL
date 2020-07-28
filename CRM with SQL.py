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
        database = "mga",
                                )

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE mga")
#print(mydb)

#my_cursor.execute("SHOW DATABASES")

#for i in my_cursor:
    #print(i)

#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(10) ,price_paid DECIMAL(10, 2),user_id INT AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)
for thing in my_cursor.description:
    print(thing)


root.mainloop()
