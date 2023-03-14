from tkinter import *
import os
import shutil
import sqlite3
from cryptography.fernet import Ferne

window = Tk()
window.title("Doge Register")
height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")


def main():
  os.system('python login_page.py')


def main_destroy():
  global youdidit
  youdidit.destroy()
  window.destroy()
  os.system('python login_page.py')


# ================ Global Variables ====================

global name1
global name2
global username
global password
global password2
global key = os.environ['key']  # "secret key" This must be kept secret
global cipher_suite = Fernet(key)  # This class provides both encryption and decryption facilities.

name1 = StringVar()
name2 = StringVar()
username = StringVar()
password = StringVar()
password2 = StringVar()



def register_user():
  name1_info = name1.get()
  name2_info = name2.get()
  username_info = username.get()
  password_info = password.get()
  password_info

  file = open(username_info, "w")
  file.write(name1_info + "\n")
  file.write(name2_info + "\n")
  file.write(username_info + "\n")
  file.close()

  file = open()
  file.write(password_info)

  os.makedirs(f"login_info/{username_info}")
  shutil.move(username_info, f"login_info/{username_info}/{username_info}")

  file = open("save1", "w")
  file.write("Save slot 1 is empty")
  file.close()
  shutil.move("save1", f"login_info/{username_info}/save1")

  file = open("save2", "w")
  file.write("Save slot 2 is empty")
  file.close()
  shutil.move("save2", f"login_info/{username_info}/save2")

  file = open("save3", "w")
  file.write("Save slot 3 is empty")
  file.close()
  shutil.move("save3", f"login_info/{username_info}/save3")

  file = open("save4", "w")
  file.write("Save slot 4 is empty")
  file.close()
  shutil.move("save4", f"login_info/{username_info}/save4")

  file = open("save5", "w")
  file.write("Save slot 5 is empty")
  file.close()
  shutil.move("save5", f"login_info/{username_info}/save5")

  file = open("login_attempts", "w")
  file.write("5")
  file.close()
  shutil.move("login_attempts", f"login_info/{username_info}/login_attempts")

  registered()


# ================Background Image ====================


def end():
  win.destroy()


def invalid():
  global win
  win = Toplevel()
  window_width = 350
  window_height = 250
  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  win.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  win.title('Invalid credentials')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Invalid credentials ==================

  invalid_label = Label(win,
                        text='Invalid credentials',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=50)

  # ======= Proceed ============
  proceed = Button(win,
                   fg='#f8f8f8',
                   text='Proceed',
                   bg='#1D90F5',
                   font=("yu gothic ui", 12, "bold"),
                   relief="flat",
                   bd=0,
                   highlightthickness=0,
                   command=end,
                   activebackground="#1D90F5")
  proceed.place(x=40, y=160, width=256, height=45)


def check():
  name1_info = name1.get()
  name2_info = name2.get()
  username_info = username.get()
  password_info = password.get()
  password2_info = password2.get()

  if username_info in os.listdir('login_info'):
    match()

  elif password_info == password2_info and name1_info != "" and name2_info != "" and username_info != "" and password_info != "":
    register_user()
  else:
    invalid()


backgroundImage = PhotoImage(file="assets/image_1.png")
bg_image = Label(window, image=backgroundImage, bg="#525561")
bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets/headerText_image.png")
headerText_image_label1 = Label(bg_image,
                                image=headerText_image_left,
                                bg="#272A37")
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(bg_image,
                    text="Dog Walker Invoice Program™",
                    fg="#FFFFFF",
                    font=("yu gothic ui bold", 20 * -1),
                    bg="#272A37")
headerText1.place(x=110, y=45)

Login_headerText_image_right = PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label2 = Label(bg_image,
                                      image=Login_headerText_image_right,
                                      bg="#272A37")
Login_headerText_image_label2.place(x=430, y=45)

Login_headerText2 = Label(bg_image,
                          anchor="nw",
                          text="From the creators™ of CALC.EXE™",
                          fg="#FFFFFF",
                          font=("yu gothic ui Bold", 20 * -1),
                          bg="#272A37")
Login_headerText2.place(x=480, y=45)

# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(bg_image,
                             text="Create new account",
                             fg="#FFFFFF",
                             font=("yu gothic ui Bold", 28 * -1),
                             bg="#272A37")
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(bg_image,
             text="Already a member?",
             fg="#FFFFFF",
             font=("yu gothic ui Regular", 15 * -1),
             bg="#272A37")
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
  bg_image,
  text="Login",
  fg="#206DB4",
  font=("yu gothic ui Bold", 15 * -1),
  bg="#272A37",
  bd=0,
  #cursor="hand2",
  highlightthickness=0,
  pady=0,
  activebackground="#272A37",
  activeforeground="#ffffff",
  command=main)
switchLogin.place(x=230, y=182, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets/input_img.png")
firstName_image_Label = Label(bg_image, image=firstName_image, bg="#272A37")
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(firstName_image_Label,
                       text="First name",
                       fg="#FFFFFF",
                       font=("yu gothic ui SemiBold", 13 * -1),
                       bg="#3D404B")
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets/name_icon.png")
firstName_icon_Label = Label(firstName_image_Label,
                             image=firstName_icon,
                             bg="#3D404B")
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
  firstName_image_Label,
  bd=0,
  bg="#3D404B",
  highlightthickness=0,
  textvariable=name1,
  fg="white",
  font=("yu gothic ui SemiBold", 16 * -1),
)
firstName_entry.place(x=8, y=17, width=140, height=27)

# ================ Last Name Section ====================
lastName_image = PhotoImage(file="assets/input_img.png")
lastName_image_Label = Label(bg_image, image=lastName_image, bg="#272A37")
lastName_image_Label.place(x=293, y=242)

lastName_text = Label(lastName_image_Label,
                      text="Last name",
                      fg="#FFFFFF",
                      font=("yu gothic ui SemiBold", 13 * -1),
                      bg="#3D404B")
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(file="assets/name_icon.png")
lastName_icon_Label = Label(lastName_image_Label,
                            image=lastName_icon,
                            bg="#3D404B")
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
  lastName_image_Label,
  bd=0,
  bg="#3D404B",
  highlightthickness=0,
  textvariable=name2,
  fg="white",
  font=("yu gothic ui SemiBold", 16 * -1),
)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Username Section ====================
userName_image = PhotoImage(file="assets/username.png")
userName_image_Label = Label(bg_image, image=userName_image, bg="#272A37")
userName_image_Label.place(x=80, y=311)

userName_text = Label(userName_image_Label,
                      text="Username",
                      fg="#FFFFFF",
                      font=("yu gothic ui SemiBold", 13 * -1),
                      bg="#3D404B")
userName_text.place(x=25, y=0)

userName_icon = PhotoImage(file="assets/name_icon.png")
userName_icon_Label = Label(userName_image_Label,
                            image=userName_icon,
                            bg="#3D404B")
userName_icon_Label.place(x=370, y=15)

userName_entry = Entry(
  userName_image_Label,
  bd=0,
  bg="#3D404B",
  highlightthickness=0,
  textvariable=username,
  fg="white",
  font=("yu gothic ui SemiBold", 16 * -1),
)
userName_entry.place(x=8, y=17, width=354, height=27)

# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets/input_img.png")
passwordName_image_Label = Label(bg_image,
                                 image=passwordName_image,
                                 bg="#272A37")
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(passwordName_image_Label,
                          text="Password",
                          fg="#FFFFFF",
                          font=("yu gothic ui SemiBold", 13 * -1),
                          bg="#3D404B")
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets/pass_icon.png")
passwordName_icon_Label = Label(passwordName_image_Label,
                                image=passwordName_icon,
                                bg="#3D404B")
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
  passwordName_image_Label,
  bd=0,
  show="*",
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  textvariable=password,
  font=("yu gothic ui SemiBold", 16 * -1),
)
passwordName_entry.place(x=8, y=17, width=140, height=27)

# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(file="assets/input_img.png")
confirm_passwordName_image_Label = Label(bg_image,
                                         image=confirm_passwordName_image,
                                         bg="#272A37")
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = Label(confirm_passwordName_image_Label,
                                  text="Confirm Password",
                                  fg="#FFFFFF",
                                  font=("yu gothic ui SemiBold", 13 * -1),
                                  bg="#3D404B")
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(file="assets/pass_icon.png")
confirm_passwordName_icon_Label = Label(confirm_passwordName_image_Label,
                                        image=confirm_passwordName_icon,
                                        bg="#3D404B")
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
  confirm_passwordName_image_Label,
  bd=0,
  show="*",
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  textvariable=password2,
  font=("yu gothic ui SemiBold", 16 * -1),
)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(file="assets/button_1.png")
submit_button = Button(bg_image,
                       image=submit_buttonImage,
                       borderwidth=0,
                       highlightthickness=0,
                       relief="flat",
                       activebackground="#272A37",
                       command=check)
submit_button.place(x=130, y=460, width=333, height=65)


def registered():
  print("Program update: Account creation success")
  global youdidit
  youdidit = Toplevel()
  window_width = 350
  window_height = 250
  screen_width = youdidit.winfo_screenwidth()
  screen_height = youdidit.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  youdidit.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  youdidit.title('Doge Success')
  youdidit.configure(background='#272A37')
  youdidit.resizable(False, False)

  # ====  Account creation successful ==================

  invalid_label = Label(youdidit,
                        text='Account created.',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=50)

  # ======= Proceed ============
  proceed = Button(youdidit,
                   fg='#f8f8f8',
                   text='Proceed',
                   bg='#1D90F5',
                   font=("yu gothic ui", 12, "bold"),
                   relief="flat",
                   bd=0,
                   highlightthickness=0,
                   command=main_destroy,
                   activebackground="#1D90F5")
  proceed.place(x=40, y=160, width=256, height=45)


def match():
  global win
  win = Toplevel()
  window_width = 350
  window_height = 250
  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  win.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  win.title('Username taken')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Username taken ==================

  invalid_label = Label(win,
                        text='Username taken.',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=50)

  # ======= Proceed ============
  proceed = Button(win,
                   fg='#f8f8f8',
                   text='Proceed',
                   bg='#1D90F5',
                   font=("yu gothic ui", 12, "bold"),
                   relief="flat",
                   bd=0,
                   highlightthickness=0,
                   command=end,
                   activebackground="#1D90F5")
  proceed.place(x=40, y=160, width=256, height=45)


window.resizable(False, False)
window.mainloop()
