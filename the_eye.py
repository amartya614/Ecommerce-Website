from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
root.geometry('1400x1400')
root.configure(background='light blue')
root.title('THE EYE')
con=sqlite3.Connection('mydb')
cur=con.cursor()
cur.execute("create table if not exists accounts(id varchar(10) Primary Key,password varchar(10),fname varchar(30),age number,gender varchar(1))")
cur.execute("create table if not exists products(pname varchar(20),price number)")
cur.execute("create table if not exists myproducts(id varchar(20),pname varchar(20),price number)")
Label(root,text='WELCOME TO SELLSOULS.COM',font="Arial 20 bold ",bd=2,bg="light blue",fg='blue',relief='ridge').pack()
image1=PhotoImage(file="theye1.gif")
lb=Label(root,image=image1)
lb.pack()

Label(root,text='Enter Username',font="Arial 20 bold",fg="blue",bg='light blue').pack()
a=Entry(root,width=40)
a.pack()
Label(root,text='                     ',bg='light blue').pack()
Label(root,text='Enter Password',font="Arial 20 bold",fg="blue",bg='light blue').pack()
c=Entry(root,show='*')
c.pack()

def create():
    window2 = Toplevel(root)
    window2.geometry('600x600')
    window2.configure(background='light blue')
    Label(window2,text="              ",font="Arial 20 bold",fg="blue",bg='light blue').pack()
    Label(window2,text='User name',font="Arial 15 bold",fg="blue",bg='light blue').pack()
    a=Entry(window2,width=30)
    a.pack() 
    Label(window2,text='Enter Password',font="Arial 15 bold",fg="blue",bg='light blue').pack()
    c=Entry(window2,show='*',width=30)
    c.pack()
    Label(window2,text='Enter your full name',font="Arial 15 bold",fg="blue",bg='light blue').pack()
    l=Entry(window2,width=30)
    l.pack()
    Label(window2,text='AGE',font="Arial 15 bold",fg="blue",bg='light blue').pack()
    d=Entry(window2,width=30)
    d.pack()
    Label(window2,text='Gender',font="Arial 15 bold",fg="blue",bg='light blue').pack()
    v1=IntVar()
    r=Radiobutton(window2,text='Male',font="Arial 15 bold",fg="blue",bg='light blue',variable=v1,value=1)
    r.pack()
    r1=Radiobutton(window2,text='Female',font="Arial 15 bold",fg="blue",bg='light blue',variable=v1,value=2)
    r1.pack()


    
    def account():
        i=0
        if a.get()=='' or c.get()=='' or d.get()=='' or l.get()=='' :
            showerror('missing input','please fill every detail')
        else:
            if (v1.get()==1):
                f='M'
            if (v1.get()==2):
                f='F'
            try:
                val=int(d.get())
                cur.execute("insert into accounts values (?,?,?,?,?)",(a.get(),c.get(),l.get(),d.get(),f))
                con.commit()
            
            except ValueError:
                showerror('error','Age is invalid')
                i=1
            except sqlite3.IntegrityError:
                showerror('error','invalid input by the user')
                i=1
            except:
                showerror('username not unique','username already exisits')
                i=1
            if(i==0):
                showinfo('welcome','account is created')
                window2.destroy()
    Button(window2,text='Create account',font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=account).pack()

def login():
    cur.execute(('SELECT * FROM accounts WHERE id = ? and password = ?'),[(a.get()),(c.get())])
    g=cur.fetchall()
    if g:
        
        if(a.get()=='theye'):
            def add():
                cur.execute('INSERT into products values (?,?)',(pn.get(),pp.get()))
                con.commit()
            window3=Toplevel(root)
            window3.geometry('600x600')
            window3.configure(background='light blue')
            Label(window3,text='Product name',font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=0,column=0)
            pn=Entry(window3)
            pn.grid(row=0,column=1)
            Label(window3,text='Product Price',font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=1,column=0)
            pp=Entry(window3)
            pp.grid(row=1,column=1)
            Button(window3,text='Add Product',font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=add).grid(row=2,column=0,columnspan=2)
            

        else:
            def cart():
                
                j=0
                
                for k in x:
                    if(v1.get()==j):
                        n=x[j][0]
                        p=x[j][1]
                        try:
                            cur.execute('INSERT into myproducts values (?,?,?)',(a.get(),n,p))
                            con.commit()
                            showinfo("cart",'item sucessfully added to cart')
                        except:
                            showerror("error","error")
                    j=j+1
                    
            def orders():
                window5=Toplevel(window4)
                window5.geometry('800x800')
                window5.configure(background='light blue')
                cur.execute("SELECT * FROM myproducts where id=?",[(a.get())])
                r=cur.fetchall()
                Label(window5,text="    Products",font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=0,column=0)
                Label(window5,text="    Price",font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=0,column=1)
                if(r==[]):
                    showerror('cart',"No items in cart")
                    window5.destroy()
                else:
                    j=0
                    for po in r:
                        Label(window5,text=r[j][1],font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=j+1,column=0)
                        Label(window5,text='Rs.'+str(r[j][2]),font="Arial 15 bold",bd=5,bg='light blue',fg='blue').grid(row=j+1,column=1)
                        j=j+1
                    cur.execute("select  sum(price) from myproducts where id=?",[(a.get())])
                    q=cur.fetchall()
                    Label(window5,text='. . . . . . . . . . . . . . . . . . . . . . .',font="Arial 15 bold",bd=3,bg='light blue',fg='blue').grid(row=j+1,column=0,columnspan=2)
                    Label(window5,text=" Total Price",font="Arial 15 bold",bg='light blue',fg='blue',bd=3,relief='ridge').grid(row=j+2,column=0)
                    Label(window5,text='Rs'+str(q[0]),font="Arial 15 bold",bd=3,bg='light blue',fg='blue',relief='ridge').grid(row=j+2,column=1)

            window4=Toplevel(root)
            window4.geometry('800x800')
            window4.configure(background='light blue')
            cur.execute(('Select * from products'))
            x=cur.fetchall()
            j=0
            h=[]
            v1=IntVar()
            for k in x:
                
                Label(window4,text=x[j][0],font="Arial 15 bold",bd=3,bg='light blue',fg='blue').pack()
                Label(window4,text='Rs.'+str(x[j][1]),font="Arial 15 bold",bd=3,bg='light blue',fg='blue').pack()

            
                h=Radiobutton(window4,text='choose to buy',font="Arial 15 bold",bd=3,bg='light blue',fg='blue',variable=v1,value=j)
                h.pack()
                Label(window4,text='. . . . . . . . . . . . . . . . .',font="Arial 15 bold",bd=3,bg='light blue',fg='blue').pack()
                j=j+1
            Button(window4,text='Add to cart',font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=cart).pack() 
            Button(window4,text="Go to Cart",font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=orders).pack()            
    else:
        showerror('invalid user','invalid username or password')

Label(root,text='                 ',bg='light blue').pack()
Button(root,text='Login',font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=login).pack()

Label(root,text='..............................................',bg='light blue').pack()
Button(root,text='Create Account',font="Arial 10 bold",bd=5,bg='light blue',fg='blue',command=create).pack()
Label(root,text='..............................................',bg='light blue').pack()


root.mainloop()


