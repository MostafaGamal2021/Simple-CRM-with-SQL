from tkinter import *
import mysql.connector
import csv
from tkinter import ttk

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
    #user_id_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def add():
    sql_command = "INSERT INTO customers (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (first_name_box.get(),last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(),address1_box.get(),address2_box.get(),city_box.get(),state_box.get(),country_box.get(),phone_box.get(),payment_method_box.get(),discount_code_box.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear()

def write_to_csv(result):
    with open('customer.csv', 'a') as f:
        w = csv.writer(f, dialect = 'excel')
        w.writerows(result)

def search():
    search_window = Tk()
    search_window.title("Search Customers")
    search_window.geometry("950x400")
    search_window.iconbitmap("D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images/plane.ico")

    def search_now():
        global searched_label
        selected = drop.get()
        global sql
        sql = ""
        if selected == "Search by ...":
            pass
        elif selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
        elif selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
        elif selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"

        searched = search_box.get()
        name = (searched,)
        my_cursor.execute(sql, name)
        global result2
        result2 = my_cursor.fetchall()
        if result2:
            list = []
            for i in result2:
                list.append(str(i)+"\n")
            searched_label = Label(search_window, text=list)
            searched_label.grid(row=5, column=2)
            csv_butn = Button(search_window, text="Save to Excel", command=lambda: write_to_csv(result2))
            csv_butn.grid(row=4 , column=1, padx=10, ipadx = 20)
        else:
            searched_label = Label(search_window, text="No record found")
            searched_label.grid(row=5, column=2)


    search_box = Entry(search_window)
    search_box.grid(row = 0, column = 1, padx = 10, pady = 10)
    search_box_label = Label(search_window, text = "Search")
    search_box_label.grid(row = 0, column = 0, padx = 10, pady = 10)
    search_btn = Button(search_window, text = "Search Now", command = search_now)
    search_btn.grid(row = 1, column = 0, columnspan = 2, padx = 10)
    drop = ttk.Combobox(search_window, value = ["Search by ...","Last Name","Email Address","Customer ID"])
    drop.current(0)
    drop.grid(row = 0, column = 2)

    def clear():
        global searched_label
        if searched_label:
            searched_label.grid_forget()
        if search_box:
            search_box.delete(0, END)

    clear_btn = Button(search_window, text="Clear", command=clear)
    clear_btn.grid(row=2, column=0, columnspan=2, padx=10)

def show_list():
    show_list_window = Tk()
    show_list_window.title("My DB List")
    show_list_window.geometry("850x500")
    show_list_window.iconbitmap("D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images/plane.ico")

    def edit():
        search_window2 = Toplevel()
        search_window2.title("Update Record")
        search_window2.geometry("400x500")
        search_window2.iconbitmap("D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images/plane.ico")
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        searched2 = id_box2.get()
        name2 = (searched2,)
        result3 = my_cursor.execute(sql2, name2)
        result3 = my_cursor.fetchall()

        first_name_label2 = Label(search_window2, text="First Name").grid(row=index+2, column=0, sticky=W, padx=10)
        last_name_label2 = Label(search_window2, text="Last Name").grid(row=index+3, column=0, sticky=W, padx=10)
        address1_label2 = Label(search_window2, text="Address 1").grid(row=index+4, column=0, sticky=W, padx=10)
        address2_label2 = Label(search_window2, text="Address 2").grid(row=index+5, column=0, sticky=W, padx=10)
        city_label2 = Label(search_window2, text="City").grid(row=index+6, column=0, sticky=W, padx=10)
        state_label2 = Label(search_window2, text="State").grid(row=index+7, column=0, sticky=W, padx=10)
        zipcode_label2 = Label(search_window2, text="Zip Code").grid(row=index+8, column=0, sticky=W, padx=10)
        country_label2 = Label(search_window2, text="Country").grid(row=index+9, column=0, sticky=W, padx=10)
        phone_label2 = Label(search_window2, text="Phone").grid(row=index+10, column=0, sticky=W, padx=10)
        email_label2 = Label(search_window2, text="Email").grid(row=index+11, column=0, sticky=W, padx=10)
        user_id_label2 = Label(search_window2, text = "User ID").grid(row = index+12, column = 0, sticky = W, padx = 10)
        payment_method_label2 = Label(search_window2, text="Payment Method").grid(row=index+13, column=0, sticky=W, padx=10)
        discount_code_label2 = Label(search_window2, text="Discount Code").grid(row=index+14, column=0, sticky=W, padx=10)
        price_paid_label2 = Label(search_window2, text="Price Paid").grid(row=index+15, column=0, sticky=W, padx=10)

        global first_name_box2
        first_name_box2 = Entry(search_window2)
        first_name_box2.grid(row=index+2, column=1, pady=5)
        first_name_box2.insert(0, result3[0][0])

        global last_name_box2
        last_name_box2 = Entry(search_window2)
        last_name_box2.grid(row=index+3, column=1, pady=5)
        last_name_box2.insert(0, result3[0][1])

        global address1_box2
        address1_box2 = Entry(search_window2)
        address1_box2.grid(row=index+4, column=1, pady=5)
        address1_box2.insert(0, result3[0][6])

        global address2_box2
        address2_box2 = Entry(search_window2)
        address2_box2.grid(row=index+5, column=1, pady=5)
        address2_box2.insert(0, result3[0][7])

        global city_box2
        city_box2 = Entry(search_window2)
        city_box2.grid(row=index+6, column=1, pady=5)
        city_box2.insert(0, result3[0][8])

        global state_box2
        state_box2 = Entry(search_window2)
        state_box2.grid(row=index+7, column=1, pady=5)
        state_box2.insert(0, result3[0][9])

        global zipcode_box2
        zipcode_box2 = Entry(search_window2)
        zipcode_box2.grid(row=index+8, column=1, pady=5)
        zipcode_box2.insert(0, result3[0][2])

        global country_box2
        country_box2 = Entry(search_window2)
        country_box2.grid(row=index+9, column=1, pady=5)
        country_box2.insert(0, result3[0][10])

        global phone_box2
        phone_box2 = Entry(search_window2)
        phone_box2.grid(row=index+10, column=1, pady=5)
        phone_box2.insert(0, result3[0][11])

        global email_box2
        email_box2 = Entry(search_window2)
        email_box2.grid(row=index+11, column=1, pady=5)
        email_box2.insert(0, result3[0][5])

        global user_id_box2
        user_id_box2 = Entry(search_window2)
        user_id_box2.grid(row = index+12, column = 1, pady = 5)
        user_id_box2.insert(0, result3[0][4])

        global payment_method_box2
        payment_method_box2 = Entry(search_window2)
        payment_method_box2.grid(row=index+13, column=1, pady=5)
        payment_method_box2.insert(0, result3[0][12])

        global discount_code_box2
        discount_code_box2 = Entry(search_window2)
        discount_code_box2.grid(row=index+14, column=1, pady=5)
        discount_code_box2.insert(0, result3[0][13])

        global price_paid_box2
        price_paid_box2 = Entry(search_window2)
        price_paid_box2.grid(row=index+15, column=1, pady=5)
        price_paid_box2.insert(0, result3[0][3])

        def update():
            sql_command = """UPDATE customers SET first_name = %s ,last_name = %s ,zipcode = %s ,price_paid = %s ,email = %s ,address_1 = %s ,address_2 = %s ,city = %s ,state = %s ,country = %s ,phone = %s ,payment_method = %s ,discount_code = %s WHERE user_id = %s"""
            first_name = first_name_box2.get()
            last_name = last_name_box2.get()
            zipcode = zipcode_box2.get()
            price_paid = price_paid_box2.get()
            email = email_box2.get()
            address_1 = address1_box2.get()
            address_2 = address2_box2.get()
            city = city_box2.get()
            state = state_box2.get()
            country = country_box2.get()
            phone = phone_box2.get()
            payment_method = payment_method_box2.get()
            discount_code = discount_code_box2.get()
            id_value = searched2

            inputs = (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code,id_value)

            my_cursor.execute(sql_command, inputs)
            mydb.commit()

            id_box2.delete(0, END)
            search_window2.destroy()
            show_list_window.destroy()

        update_butn = Button(search_window2, text="Update Record", command=update)
        update_butn.grid(row=index + 17, column=0, padx=20)

    my_cursor.execute("SELECT * FROM customers")
    results = my_cursor.fetchall()
    for index, x in enumerate(results): # "enumerate" makes an index number for each line of list
        num = 0
        for y in x:
            lookup_label = Label(show_list_window, text = y)
            lookup_label.grid(row = index, column = num)
            num += 1
    csv_butn = Button(show_list_window, text = "Save to Excel", command = lambda :write_to_csv(results))
    csv_butn.grid(row = index+1, column = 0, padx = 20)
    edt_butn = Button(show_list_window, text="Edit Record", command= edit)
    edt_butn.grid(row=index + 1, column=1, padx=20)
    id_label_2 = Label(show_list_window, text="Record ID").grid(row=index + 2, column=0, sticky=W, padx=10)
    global id_box2
    id_box2 = Entry(show_list_window)
    id_box2.grid(row=index + 2, column=1, pady=5)

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
#user_id_label = Label(root, text = "User ID").grid(row = 11, column = 0, sticky = W, padx = 10)
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
#user_id_box = Entry(root)
#user_id_box.grid(row = 11, column = 1, pady = 5)
payment_method_box = Entry(root)
payment_method_box.grid(row = 12, column = 1, pady = 5)
discount_code_box = Entry(root)
discount_code_box.grid(row = 13, column = 1, pady = 5)
price_paid_box = Entry(root)
price_paid_box.grid(row = 14, column = 1, pady = 5)

add_customer_button = Button(root, text = "Add Customer to Database", command = add)
add_customer_button.grid(row = 15, column = 0, columnspan = 2, pady = (10,5) , padx = 10, ipady = 5, ipadx = 35)
clear_button = Button(root, text = "Clear", command = clear)
clear_button.grid(row = 17, column = 0, columnspan = 2, pady = 5, padx = 10, ipadx = 51)
show_button = Button(root, text = "Show List", command = show_list)
show_button.grid(row = 16, column = 0, columnspan = 2, padx = 10, ipadx = 40)
search_btn = Button(root, text = "Search Customers", command = search)
search_btn.grid(row = 18, column = 0, columnspan = 2, padx = 10, ipadx = 40)


root.mainloop()
