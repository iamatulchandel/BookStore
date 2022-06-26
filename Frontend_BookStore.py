from tkinter import *
from BackEndBookStore import *
window = Tk()
window.wm_title('BookSTore')

def get_selected(event):
    try:
        global selected_tuple
        index=l1.curselection()[0]
        selected_tuple=l1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[0])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[3])
    except IndexError:
        pass


def View_All():
    l1.delete('0',END)
    for i in view():
        l1.insert(END,i)
def insert_op():
    INSERTtable(title1.get(),auth1.get(),year1.get(),isbn.get())
    l1.delete('0',END)
    l1.insert(END,(title1.get(),auth1.get(),year1.get(),isbn.get()))
def search_entry():
    op=SEARCHEntry(title1.get(),auth1.get(),year1.get(),isbn.get())
    l1.delete('0', END)
    for i in op:
        l1.insert(END, i)
def update_op():
    UPDATEentry(title1.get(),auth1.get(),year1.get(),isbn.get())
    l1.delete('0',END)
    l1.insert(title1.get(),auth1.get(),year1.get(),isbn.get())
def delete_op():
    DELETEentry(selected_tuple[0])
L1= Label(window, text='Title')
L1.grid(row=0,column=0)
L2= Label(window,text='Year')
L2.grid(row=1,column=0)
L3= Label(window,text='Author')
L3.grid(row=0,column=3)
L4= Label(window,text='ISBN')
L4.grid(row=1,column=3)
title1=StringVar()
e1=Entry(window,textvariable=title1)
e1.grid(row=0,column=1)
year1=StringVar()
e2=Entry(window,textvariable=year1)
e2.grid(row=1,column=1)
auth1=StringVar()
e3=Entry(window,textvariable=auth1)
e3.grid(row=0,column=4)
isbn=StringVar()
e4=Entry(window,textvariable=isbn)
e4.grid(row=1,column=4)
l1 = Listbox(window,height=7,width=35)
l1.grid(row=2,column=0,rowspan=7,columnspan=2)
s1 = Scrollbar()
s1.grid(row=2,column=2,rowspan=6)
l1.configure(yscrollcommand=s1.set)
s1.configure(command=l1.yview())
l1.bind('<<ListboxSelect>>',get_selected)
b1=Button(window,text='View  All',width=12,command=View_All)
b1.grid(row=2,column=4)
b2=Button(window,text='Search Entry',width=12,command=search_entry)
b2.grid(row=3,column=4)
b3=Button(window,text='Add Entry',width=12,command=insert_op)
b3.grid(row=4,column=4)
b4=Button(window,text='Update',width=12,command=update_op)
b4.grid(row=5,column=4)
b5=Button(window,text='Delete',width=12,command=delete_op)
b5.grid(row=6,column=4)
b6=Button(window,text='CLose',width=12,command=window.destroy)
b6.grid(row=7,column=4)

window.mainloop()
