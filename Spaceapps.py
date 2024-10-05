import tkinter as tk
from tkinter import Entry
import ttkbootstrap as ttk



def button():
    def signin():
        result_label.config(text="Signed Up")


        
    root=tk.Tk()
    root.geometry("800x550")
    root.title("Sign Up") 
    
    Name_label = tk.Label(root, text="Name",font="Arial,18,bold")
    Name_label.pack(padx=10,pady=10)

    Name_entry=tk.Entry(root)
    Name_entry.pack(padx=5,pady=5)

    Email_label = tk.Label(root, text="Email:",font="Arial,18,bold")
    Email_label.pack(padx=10,pady=10)

    Email_entry = tk.Entry(root)
    Email_entry.pack(padx=5,pady=5) 

  
    password_label = tk.Label(root, text="Password:",font="Arial,50,bold")
    password_label.pack(pady=10)

    password_entry=tk.Entry(root)
    password_entry.pack(padx=5,pady=5)

    Cpassword_label=tk.Label(root,text="Confirm Password:",font="Arial,18,bold")
    Cpassword_label.pack(padx=10,pady=10)

    Cpassword_entry=tk.Entry(root)
    Cpassword_entry.pack(padx=5,pady=5)

    
    

    Signup_button = tk.Button(root, text="Sign Up" ,width=50,height=2,command=signin)
    Signup_button.pack(pady=10)


    result_label = tk.Label(root, text="",font="Arial,50,bold")
    result_label.pack(pady=10)

   
   
    root.mainloop()




root1=ttk.Window(themename = 'darkly')
root1.geometry("800x500")
root1.title("AGRO APP")

label=tk.Label(root1,text="Select your operation",font="Arial,50,bold")
label.pack(pady=50)
 
btn2=tk.Button(root1,text="Sign Up",font=("AriaL,40,bold"),width=50,height=2,fg="Orange",bd=8,bg="black",command=button)
btn2.pack(padx=10,pady=10)

btn3=tk.Button(root1,text="News",font=("AriaL,20"),width=50,height=2,fg="red",bd=8,bg="black")
btn3.pack(padx=10,pady=10)

btn4=tk.Button(root1,text="Current Climate",font=("AriaL,20"),width=50,height=2,fg="red",bd=8,bg="black")
btn4.pack(padx=10,pady=10)

btn1=tk.Button(root1,text="Chat with Others",font=("AriaL,20"),width=50,height=2,fg="red",bd=8,bg="black")
btn1.pack(padx=10,pady=10)

btn1=tk.Button(root1,text="Talk to your assistant",font=("AriaL,20"),width=50,height=2,fg="red",bd=8,bg="black")
btn1.pack(padx=10,pady=10)





root1.mainloop()