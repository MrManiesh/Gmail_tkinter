from tkinter import *
import conn

main_win = Tk()
main_win.geometry('700x700')
main_win.title("LogIn")
main_win.resizable(0,0)

#SignIn form
def SignIn(label_12_text=""):
    signin_frame = Frame(main_win)
    signin_frame.place(x=0, y=0, width=700, height=700)

    label_9 = Label(signin_frame, text="Login",width=20,font=("bold", 20))
    label_9.place(x=160,y=100)
    
    label_12 = Label(signin_frame,text=label_12_text,width=30, fg="red",font=("bold", 8))
    label_12.place(x=215,y=225)

    label_10 = Label(signin_frame, text="Username/Email : ",width=25)
    label_10.place(x=50,y=250)
    ent9=Entry(signin_frame, width=25)
    ent9.place(x=230,y=250)

    label_11 = Label(signin_frame, text="Password : ",width=25)
    label_11.place(x=50,y=320)
    ent10=Entry(signin_frame, width=25, show="*")
    ent10.place(x=230,y=320)
    
    Button(signin_frame, text='Sign In',width=17,bg='brown',fg='white', command = lambda : check_login_validation(ent9.get(), ent10.get(),signin_frame,label_12)).place(x=180,y=380)

#form vaslidation 
def check_login_validation(username, passwd,signin_frame, label_12):
        username = username.lower()
        if ("@qmail.com" in username):
            username = username[:-10] #removing @qmail.com 

        try:  
            if (username == conn.get_data(username)[5]) and (passwd == conn.get_data(username)[6]):
                first_page(username,signin_frame)
            else:
                SignIn(label_12_text="*invalid Username/Email or Password")

        except:
            SignIn(label_12_text="*invalid Username/Email or Password")

# welcome screen after login
def first_page(username,signin_frame):
    signin_frame.destroy()
    msg1 = "Hello {}, \nWelcome to QMail".format(conn.get_data(username)[0])
    first_frame = Frame(main_win)
    first_frame.place(x=0, y=0, width=500, height=500)

    label_13 = Label(first_frame, text=msg1,width=20,font=("bold", 12))
    label_13.place(x=90,y=53)
SignIn()

main_win.mainloop()









