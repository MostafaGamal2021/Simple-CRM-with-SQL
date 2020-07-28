from tkinter import *
import mysql.connector


root = Tk()
root.title('MGA')
root.geometry('320x600')
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

'''
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    zipcode INT(10) ,
                    price_paid DECIMAL(10, 2),
                    user_id INT AUTO_INCREMENT PRIMARY KEY)""")

my_cursor.execute("""ALTER TABLE customers ADD (
                    email VARCHAR(255),
                    address_1 VARCHAR(255),
                    address_2 VARCHAR(255),
                    city VARCHAR(50),
                    state VARCHAR(50),
                    country VARCHAR(255),
                    phone VARCHAR(255),
                    payment_method VARCHAR(50),
                    discount_code VARCHAR(255)
                    )""")
'''

#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)
#for thing in my_cursor.description:
    #print(thing)
#my_cursor.execute("DROP TABLE customers")
def clear():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    user_id_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

title_label = Label(root, text = "MGA Customers Database", font = ("Helvetica", 16), fg = "blue")
title_label.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 10)

first_name_label = Label(root, text = "First Name").grid(row = 1, column = 0, sticky = W, padx = 10)
last_name_label = Label(root, text = "Last Name").grid(row = 2, column = 0, sticky = W, padx = 10)
address1_label = Label(root, text = "Address 1").grid(row = 3, column = 0, sticky = W, padx = 10)
address2_label = Label(root, text = "Address 2").grid(row = 4, column = 0, sticky = W, padx = 10)
city_label = Label(root, text = "City").grid(row = 5, column = 0, sticky = W, padx = 10)
state_label = Label(root, text = "State").grid(row = 6, column = 0, sticky = W, padx = 10)
zipcode_label = Label(root, text = "Zip Code").grid(row = 7, column = 0, sticky = W, padx = 10)
country_label = Label(root, text = "Country").grid(row = 8, column = 0, sticky = W, padx = 10)
phone_label = Label(root, text = "Phone").grid(row = 9, column = 0, sticky = W, padx = 10)
email_label = Label(root, text = "Email").grid(row = 10, column = 0, sticky = W, padx = 10)
user_id_label = Label(root, text = "User ID").grid(row = 11, column = 0, sticky = W, padx = 10)
payment_method_label = Label(root, text = "Payment Method").grid(row = 12, column = 0, sticky = W, padx = 10)
discount_code_label = Label(root, text = "Discount Code").grid(row = 13, column = 0, sticky = W, padx = 10)
price_paid_label = Label(root, text = "Price Paid").grid(row = 14, column = 0, sticky = W, padx = 10)

first_name_box = Entry(root)
first_name_box.grid(row = 1, column = 1, pady = 5)
last_name_box = Entry(root)
last_name_box.grid(row = 2, column = 1, pady = 5)
address1_box = Entry(root)
address1_box.grid(row = 3, column = 1, pady = 5)
address2_box = Entry(root)
address2_box.grid(row = 4, column = 1, pady = 5)
city_box = Entry(root)
city_box.grid(row = 5, column = 1, pady = 5)
state_box = Entry(root)
state_box.grid(row = 6, column = 1, pady = 5)
zipcode_box = Entry(root)
zipcode_box.grid(row = 7, column = 1, pady = 5)
country_box = Entry(root)
country_box.grid(row = 8, column = 1, pady = 5)
phone_box = Entry(root)
phone_box.grid(row = 9, column = 1, pady = 5)
email_box = Entry(root)
email_box.grid(row = 10, column = 1, pady = 5)
user_id_box = Entry(root)
user_id_box.grid(row = 11, column = 1, pady = 5)
payment_method_box = Entry(root)
payment_method_box.grid(row = 12, column = 1, pady = 5)
discount_code_box = Entry(root)
discount_code_box.grid(row = 13, column = 1, pady = 5)
price_paid_box = Entry(root)
price_paid_box.grid(row = 14, column = 1, pady = 5)

add_customer_button = Button(root, text = "Add Customer to Database")
add_customer_button.grid(row = 15, column = 0, columnspan = 2, pady = 10, padx = 10, ipady = 7, ipadx = 35)
clear_button = Button(root, text = "Clear", command = clear)
clear_button.grid(row = 16, column = 0, columnspan = 2, padx = 10, ipadx = 30)

root.mainloop()
