import tkinter as t
from tkinter import messagebox
import random
import pyperclip3  # Module to help with clipboard functions.

#####################  CONSTANTS  ####################
dark1 = "#2C3333"
dark2 = "#395B64"
light1 = "#E7F6F2"
light2 = "#A5C9CA"
font1 = ("Times New Roman", 13, 'bold')
font2 = ("Times New Roman", 13, 'normal')
################################  PASSWORD GENERATOR  ##############################
list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ["0","1","2","3","4","5","6","7","8","9"]
list_symbols = ["!","#","$","%","&","(",")","*","+"]

def gen_password():
    n_letters = random.randint(3, 8)
    n_numbers = random.randint(1, 3)
    n_symbols = random.randint(1, 2)
    
    # Clear previous information from password entry.
    e_pass.delete(0, t.END)

    new_password = []
    # Can also use list comprehension, but more lists would be used.
    for i in range(n_letters):
        new_password.append(random.choice(list_letters))
    for i in range(n_numbers):
        new_password.append(random.choice(list_numbers))
    for i in range(n_symbols):
        new_password.append(random.choice(list_symbols))
    
    random.shuffle(new_password)
    # Write string to password entry.
    e_pass.insert(t.END, "".join(new_password))

#############################  SAVE PASSWORD  #################################
def add_password():
    ###############  Message box (pop-ups)  ##################
    # Check for empty fields.
    if(e_pass.get() == '' or e_uid.get() == '' or e_website.get() == ''):
        # Show a pop-up warning.
        messagebox.showinfo(title='Oops....', message="Please don't leave any fields empty!")
        
    else:
        # Ask user to confirm details (Either True or False).
        response = messagebox.askokcancel(title='Check Info', message=f"Is this correct?\n\nWebsite: {e_website.get()}\nUsername: {e_uid.get()}\nPassword: {e_pass.get()}")
        if(response == True):    
            # Copy to clipboard, the contents of the password field (using pyperclip module).
            pyperclip3.copy(e_pass.get())
            
            # Write to file (append at end).
            with open('./passwords.txt', mode='a') as file:
                file.write(e_website.get() + " | " + e_uid.get() + " | " + e_pass.get() + "\n")    

            # Clear current text entry fields.
            e_website.delete(0, t.END)
            e_uid.delete(0, t.END)
            e_pass.delete(0, t.END)

###############################  UI SETUP  ####################################
# Set up a window.
window = t.Tk()
window.config(padx=25, pady=25, bg=dark1)
window.title('Password Mananger')

# Set canvas widget for image.
img = t.Canvas(width=200, height=200)
img_file = t.PhotoImage(file='./logo.png')
img.create_image(100, 100, image=img_file)
img.config(bg=dark1, highlightthickness=0)
img.grid(column=1, row=0)

# Label for website name.
l_website = t.Label(text='Website:', highlightthickness=0, bg=dark1, fg=light1, font=font1)
l_website.grid(column=0, row=1)

# Label for Email/Username.
l_uid = t.Label(text='Username/Email:', highlightthickness=0, bg=dark1, fg=light1, font=font1)
l_uid.grid(column=0, row=2)

# Label for Password.
l_pass = t.Label(text='Password:', highlightthickness=0, bg=dark1, fg=light1, font=font1)
l_pass.grid(column=0, row=3)

# Entry for website.
e_website = t.Entry()
e_website.config(width=40, highlightthickness=0, bg=dark2, fg=light1, font=font2)
e_website.focus()  # Place cursor here initially.
# Simply streching/increasing the width would disturb other components.
e_website.grid(column=1, row=1, columnspan=2)  # To 're-scale' the widget.

# Entry for Email/Username.
e_uid = t.Entry()
e_uid.config(width=40, highlightthickness=0, bg=dark2, fg=light1, font=font2)
e_uid.grid(column=1, row=2, columnspan=2)

# Entry for Password.
e_pass = t.Entry()
e_pass.config(width=22, highlightthickness=0, bg=dark2, fg=light1, font=font2)
e_pass.grid(column=1, row=3)

# Button to generate random password.
b_gen = t.Button(text='Generate', command=gen_password, bg=light2, fg=dark1)
b_gen.config(width=22, highlightthickness=0)
b_gen.grid(column=2, row=3)

# Button to add (save) new password to a file.
b_add = t.Button(text='Add', command=add_password, bg=light2, fg=dark1)
b_add.config(width=51, highlightthickness=0)
b_add.grid(column=1, row=4, columnspan=2)

# To keep window displayed.
window.mainloop()
