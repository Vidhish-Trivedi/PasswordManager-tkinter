import tkinter as t

#####################  CONSTANTS  ####################
dark1 = "#2C3333"
dark2 = "#395B64"
light1 = "#E7F6F2"
font1 = ("Times New Roman", 13, 'bold')
font2 = ("Times New Roman", 13, 'normal')
################################  PASSWORD GENERATOR  ##############################
def gen_password():
    pass


#############################  SAVE PASSWORD  #################################
def add_password():
    with open('./passwords.txt', mode='a') as file:
        file.write(e_website.get() + " | " + e_uid.get() + " | " + e_pass.get() + "\n")
    print("written")

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
b_gen = t.Button(text='Generate', command=gen_password)
b_gen.config(width=22, highlightthickness=0)
b_gen.grid(column=2, row=3)

# Button to add (save) new password to a file.
b_add = t.Button(text='Add', command=add_password)
b_add.config(width=51, highlightthickness=0)
b_add.grid(column=1, row=4, columnspan=2)

# To keep window displayed.
window.mainloop()
