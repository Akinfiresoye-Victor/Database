from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root=Tk()
root.title('databases')
#root.iconbitmap('c://Users//user//Downloads//frog.ico')
root.geometry('500x500')

#creating a database
conn= sqlite3.connect('address_book.db')

#creating a cursor
cursor= conn.cursor()
#' create tables according to their format text, integer, real, 
#cursor.execute('''CREATE TABLE addresses(
#    First_name text,
#     last_name text,
 ##  adress text,
#    city text,
#    state text,
 #   zipcode integer
#    )''')

#creating textboxes for the above values
f_name=Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20)

l_name=Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)

address=Entry(root, width=30)
address.grid(row=2,column=1, padx=20)

city=Entry(root, width=30)
city.grid(row=3,column=1, padx=20)

state=Entry(root, width=30)
state.grid(row=4,column=1, padx=20)

zipcode=Entry(root, width=30)
zipcode.grid(row=5,column=1, padx=20)

delete_box= Entry(root, width=30)
delete_box.grid(row=9, column=1)

#create textbox labels
f_name_label= Label(root, text='first name')
f_name_label.grid(row=0, column=0)

l_name_label= Label(root, text='last name')
l_name_label.grid(row=1, column=0)

address_label= Label(root, text='adress')
address_label.grid(row=2, column=0)

city_label= Label(root, text='city')
city_label.grid(row=3, column=0)

state_label= Label(root, text='state')
state_label.grid(row=4, column=0)

zipcode_label= Label(root, text='zipcode')
zipcode_label.grid(row=5, column=0)

delete_lbl= Label(root, text='Select ID number?')
delete_lbl.grid(row=9, column=0)
def delete():
    conn= sqlite3.connect('address_book.db')
    #Creating cursor
    cursor= conn.cursor()
    
    conn.execute("DELETE FROM addresses WHERE oid= "+ delete_box.get())
    
    conn.commit()

    #closing connection
    conn.close 

#create an update function
def update():
    editor=Tk()
    editor.title('Updated records')
    editor.iconbitmap('c://Users//user//Downloads//frog.ico')
    editor.geometry('500x500')
    #submitting it
    conn= sqlite3.connect('address_book.db')
    #Creating cursor
    cursor= conn.cursor()
    
    record_id=delete_box
    cursor.execute('SELECT * FROM addresses WHERE oid=*')
    records= cursor.fetchall()
    
    #loop through results
    print_records='' 
    for record in records:
        print_records += str(record) + '\n'    
#creating textboxes for the above values
    f_name_upd=Entry(editor, width=30)
    f_name_upd.grid(row=0,column=1, padx=20)
    l_name_upd=Entry(editor, width=30)
    l_name_upd.grid(row=1,column=1, padx=20)

    address_upd=Entry(editor, width=30)
    address_upd.grid(row=2,column=1, padx=20)

    city_upd=Entry(editor, width=30)
    city_upd.grid(row=3,column=1, padx=20)

    state_upd=Entry(editor, width=30)
    state_upd.grid(row=4,column=1, padx=20)

    zipcode_upd=Entry(editor, width=30)
    zipcode_upd.grid(row=5,column=1, padx=20)

    #create textbox labels
    f_name_label= Label(editor, text='first name')
    f_name_label.grid(row=0, column=0)

    l_name_label= Label(editor, text='last name')
    l_name_label.grid(row=1, column=0)

    address_label= Label(editor, text='adress')
    address_label.grid(row=2, column=0)

    city_label= Label(editor, text='city')
    city_label.grid(row=3, column=0)

    state_label= Label(editor, text='state')
    state_label.grid(row=4, column=0)

    zipcode_label= Label(editor, text='zipcode')
    zipcode_label.grid(row=5, column=0)

#Creating button to save updated records
    save_btn= Button(editor , text='Save record ', command=update)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=144)
    
    

    
#create submit function for d button
def submit():
    #submitting it
    conn= sqlite3.connect('address_book.db')
    #Creating cursor
    cursor= conn.cursor()
    
    #insert into the table
    cursor.execute('INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)',
                   {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                   })
    
    #commiting changes made into the cursor
    conn.commit()

    #closing connection
    conn.close 
    
    #clear the textboxes after submiting
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def name():
            #submitting it
    conn= sqlite3.connect('address_book.db')
    #Creating cursor
    cursor= conn.cursor()
    cursor.execute('SELECT *, oid FROM addresses')
    records= cursor.fetchall()
    
    #loop through results
    print_records='' 
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1])+ '\n'
        
        query_lbl=Label(root, text=print_records)
        query_lbl.grid(row=8, column=0, columnspan=2)
         
 #commiting changes made into the cursor
    conn.commit()

    #closing connection
    conn.close 
        




def query():
    #submitting it
    conn= sqlite3.connect('address_book.db')
    #Creating cursor
    cursor= conn.cursor()
    cursor.execute('SELECT *, oid FROM addresses')
    records= cursor.fetchall()
    
    #loop through results
    print_records='' 
    for record in records:
        print_records += str(record) + '\n'
        
    query_lbl=Label(root, text=print_records)
    query_lbl.grid(row=12, column=0, columnspan=2)
         
 #commiting changes made into the cursor
    conn.commit()

    #closing connection
    conn.close 

#creating a submit button
submit_button=Button(root, text='Add record to databese', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10,ipadx=100)

#creates a query button
query_btn= Button(root, text='show records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

delete_btn= Button(root, text=' Delete records', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#create an update button
update_btn= Button(root, text='Update record ', command=update)
update_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=144)


#commiting changes made into the cursor
conn.commit()

#closing connection
conn.close


mainloop()