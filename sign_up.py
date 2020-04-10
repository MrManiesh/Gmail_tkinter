from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb
from tkcalendar import *

import conn #importing my own files

main_win = Tk()
main_win.geometry('1000x1000')
main_win.title("QMail")
main_win.resizable(0,0)

def SignUp():
    SignUp_frame=Frame(main_win) 
    SignUp_frame.place(x=0, y=0, width=1000, height=1000)

    label_err = Label(SignUp_frame, fg="white",font=("bold", 8))
    label_err.place(x=300,y=700)

    f_name_label = Label(SignUp_frame, text="Enter your first name : ",width=25)
    f_name_label.place(x=10,y=40)
    f_name_input = Entry(SignUp_frame, width=25)
    f_name_input.place(x=220,y=40)
    f_name_err = Label(SignUp_frame, fg="red",font=("bold", 8))
    f_name_err.place(x=430,y=40)

    s_name_label = Label(SignUp_frame, text="Enter your second name : ",width=25)
    s_name_label.place(x=10,y=120)
    s_name_input = Entry(SignUp_frame, width=25)
    s_name_input.place(x=220,y=120)

    dob_label = Label(SignUp_frame, text="Enter your Date of birth : ",width=25)
    dob_label.place(x=10,y=200)
    dob_input = DateEntry(SignUp_frame, width=22, background = 'brown', foreground ='white', borderwidth = 3 )
    dob_input.place(x=220,y=200)

    mob_label = Label(SignUp_frame, text="Enter your Mobile No. : ",width=25)
    mob_label.place(x=10,y=280)
    mob_input = Entry(SignUp_frame, width=25)
    mob_input.place(x=220,y=280)
    mob_err = Label(SignUp_frame, fg="red",font=("bold", 8))
    mob_err.place(x=430,y=280)

    altr_mail_label = Label(SignUp_frame, text="Enter your Alternate Email : ",width=25)
    altr_mail_label.place(x=10,y=360)
    altr_mail_input=Entry(SignUp_frame, width=25)
    altr_mail_input.place(x=220,y=360)
    altr_mail_err = Label(SignUp_frame, fg="red",font=("bold", 8))
    altr_mail_err.place(x=430,y=360)
    
    user_id_label = Label(SignUp_frame, text=" Choose ID : ",width=25)
    user_id_label.place(x=10,y=440)
    user_id_input = Entry(SignUp_frame, width=25)
    user_id_input.place(x=220,y=440)
    uid_err = Label(SignUp_frame,width=30,font=("bold", 8))
    uid_err.place(x=450,y=440)
    Button(SignUp_frame, text='check', width=10, bg='brown', fg='white',
            command = lambda : check_id_validation(user_id_input.get(),uid_err)).place(x=440,y=435)    
    
    
    n_pass_label = Label(SignUp_frame, text="Enter password : ",width=25)
    n_pass_label.place(x=10,y=520)
    n_pass_input = Entry(SignUp_frame, width=25,show='*')
    n_pass_input.place(x=220,y=520)
    n_pass_err = Label(SignUp_frame, fg="red",font=("bold", 8))
    n_pass_err.place(x=430,y=520)

    re_pass_label = Label(SignUp_frame, text="Re-Enter password : ",width=25)
    re_pass_label.place(x=10,y=600)
    re_pass_input = Entry(SignUp_frame, width=25,show='*')
    re_pass_input.place(x=220,y=600)
    re_pass_err = Label(SignUp_frame, fg="red",font=("bold", 8))
    re_pass_err.place(x=430,y=600)

    Button(SignUp_frame, text='Submit', width=20, bg='brown', fg='white',
            command = lambda : SignUp_form_validation(f_name_input.get(), s_name_input.get(),
            dob_input.get(), mob_input.get(), altr_mail_input.get(), user_id_input.get(),
            n_pass_input.get(),re_pass_input.get(), mob_err, altr_mail_err, n_pass_err,
            re_pass_err, label_err, uid_err, SignUp_frame, f_name_err) ).place(x = 360, y = 750)

def check_id_validation(choose_id,uid_err):
    if (choose_id not in conn.get_all_user_id()) and ( (choose_id not in [""," "]) and len(choose_id)>3  ) :
        uid_err.config(text="Available", fg="green")
        return 1
    else:
        uid_err.config(text="unavailable",fg="red")
        return 0

def SignUp_form_validation(fname, lname, dob, phone_number, Alt_email, e_id, e_pass, re_pass, mob_err,
                            altr_mail_err, n_pass_err, re_pass_err, label_err, uid_err, SignUp_frame, f_name_err):
    error_val = 0

    if len(fname)<2:
        f_name_err.config(text="* Enter first name")
        error_val = error_val + 1
    else:
        f_name_err.config(text="")

    if (len(phone_number)<10):
        mob_err.config(text="* Invalid mobile number")
        error_val = error_val + 1
    else:
        mob_err.config(text="")
    
    if ("@" in Alt_email) and ("." in Alt_email):
        altr_mail_err.config(text="")
    else:
        altr_mail_err.config(text="* Invalid Valid Email ID")
        error_val = error_val + 1

    if check_id_validation(e_id,uid_err) == 0:
        uid_err.config(text="unavailable",fg="red")
        error_val = error_val + 1

    if len(e_pass)<6:
        n_pass_err.config(text="* Too sort password")
        error_val = error_val + 1
    else:
        n_pass_err.config(text="")

    if e_pass != re_pass:
            re_pass_err.config(text="* Password not matched")
            error_val = error_val + 1
    else:
        re_pass_err.config(text="")
    
    if error_val == 0:
        label_err.config(text="")
        SignUp_frame.destroy()
        save_signup_data(fname, lname, dob, phone_number, Alt_email, e_id, e_pass)
    else:
        txt = "* Total {} Errors found, Please solve them to process ".format(error_val)
        label_err.config(bg = "red", text=txt)


def save_signup_data(fname, lname, dob, phone_number, Alt_email, e_id, e_pass):
    wlcm_frame = Frame(main_win)
    wlcm_frame.place(x=0, y=0, width=500, height=500)
    label_wel = Label(wlcm_frame,font=("bold", 20))
    label_wel.place(x=90,y=53)

    try:
        conn.add_user(fname, lname, dob, phone_number, Alt_email, e_id, e_pass)
        welcome_txt = "Hey {}, \n Welcome to QMail.".format(fname)
        label_wel.config(text=welcome_txt)
    except:
        welcome_txt = "Sorry, \n Something wents wrong."
        label_wel.config(text=welcome_txt)

SignUp()   
main_win.mainloop()