# ==================== MODULES ====================

import os
import shutil
from tkinter import *
from cryptography.fernet import Fernet
from pathlib import Path


# ==================== CREATE ROOT WINDOW ====================

window = Tk()
window.title("Doge Login")
height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.configure(bg="#525561")
window.resizable(False, False)

backgroundImage = PhotoImage(file="assets/image_1.png")
bg_image = Label(window, image=backgroundImage, bg="#525561")
bg_image.place(x=120, y=28)
Login_backgroundImage = PhotoImage(file="assets/image_1.png")
bg_imageLogin = Label(window, image=Login_backgroundImage, bg="#525561")
bg_imageLogin.place(x=120, y=28)

# ==================== VARIABLES ====================

global username_verify
global password_verify
global username_login_entry
global password_login_entry
global key 
global cipher_suite

key = os.environ['key']
cipher_suite = Fernet(key)

username_login_entry = StringVar()
password_login_entry = StringVar()

# ==================== SUBROUTINES ====================

def delete_account():
  global username1
  shutil.rmtree(f"login_info/{username1}")
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

  win.title('Doge account deleted')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Account deleted ==================

  invalid_label = Label(win,
                        text='Account deleted.',
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
  
def register():
  os.system('python register_page.py')


def end():
  win.destroy()
  
def login_verify():
  global username_login_entry
  global password_login_entry
  global username1
  global password1
  username1 = username_login_entry.get()
  password1 = password_login_entry.get()
  Login_userName_entry.delete(0, END)
  Login_passwordName_entry.delete(0, END)

  list_of_files = os.listdir("login_info")
  if username1 in list_of_files:
    password_verify = Path(f"login_info/{username1}/password").read_text()
    password_verify = cipher_suite.decrypt(password_verify)
    password_verify = password_verify.decode("utf-8")
    
    if password1 == password_verify:
      login_success()
    else:
      current_attempts = Path(f"login_info/{username1}/attempts").read_text()
      int_current_attempts = int(current_attempts)
      int_current_attempts = int_current_attempts-1
      if int_current_attempts == 0:
        Login_userName_entry.delete(0, END)
        Login_passwordName_entry.delete(0, END)
        delete_account()
        
      else:
        str_current_attempts = str(int_current_attempts)
        Path(f"login_info/{username1}/attempts").write_text(str_current_attempts)
        Login_passwordName_entry.delete(0, END)
      
        password_not_recognised(str_current_attempts)
  else:
    user_not_found()
    Login_userName_entry.delete(0, END)
    Login_passwordName_entry.delete(0, END)

def login_success():
  global win
  global username1
  print(f"Program update: Logged in as: {username1}")
  Path(f"login_info/current").write_text(username1)
  Path(f"login_info/{username1}/attempts").write_text("5")
  win = Toplevel()
  window_width = 350
  window_height = 250
  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  win.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  win.title('Doge Login Success')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Login success ==================

  invalid_label = Label(win,
                        text='Login success.',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=50)

  # ======= Proceed ============
  proceed = Button(win,
                   fg='#f8f8f8',
                   text='Run program',
                   bg='#1D90F5',
                   font=("yu gothic ui", 12, "bold"),
                   relief="flat",
                   bd=0,
                   highlightthickness=0,
                   command=delete_login_success,
                   activebackground="#1D90F5")
  proceed.place(x=40, y=160, width=256, height=45)

def password_not_recognised(a):
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

  win.title('Doge Wrong Password')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  password not recognised ==================

  invalid_label = Label(win,
                        text='Wrong password.',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=50)
  invalid_label = Label(win,
                        text=f'Attempts left: {a}',
                        fg="#FFFFFF",
                        bg='#272A37',
                        font=("yu gothic ui", 20, 'bold'))
  invalid_label.place(x=40, y=100)

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


def user_not_found():
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

  win.title('Doge User Missing')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  User not found ==================

  invalid_label = Label(win,
                        text='User not found.',
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

def delete_login_success():
  win.destroy()
  os.system('python invoice_calculator.py')


def delete_password_not_recognised():
  password_not_recog_screen.destroy()


def delete_user_not_found_screen():
  user_not_found_screen.destroy()

def forgot_password():
  global username
  global password
  username = StringVar()
  password = StringVar()
  global win
  win = Toplevel()
  window_width = 350
  window_height = 350
  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  win.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  win.title('Forgot Password')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====== Username ====================
  username_entry3 = Entry(win,
                          bg="#3D404B",
                          font=("yu gothic ui semibold", 12),
                          highlightthickness=1,
                          fg="white",
                          bd=0)
  username_entry3.place(x=40, y=80, width=256, height=50)
  username_entry3.config(highlightbackground="#3D404B",
                         highlightcolor="#206DB4",
                         textvariable=username)
  username_label3 = Label(win,
                          text='• Username',
                          fg="#FFFFFF",
                          bg='#272A37',
                          font=("yu gothic ui", 11, 'bold'))
  username_label3.place(x=40, y=50)

  # ====  New Password ==================
  new_password_entry = Entry(win,
                             bg="#3D404B",
                             font=("yu gothic ui semibold", 12),
                             show='*',
                             fg="white",
                             highlightthickness=1,
                             bd=0)
  new_password_entry.place(x=40, y=180, width=256, height=50)
  new_password_entry.config(highlightbackground="#3D404B",
                            highlightcolor="#206DB4",
                            textvariable=password)
  new_password_label = Label(win,
                             text='• New Password',
                             fg="#FFFFFF",
                             bg='#272A37',
                             font=("yu gothic ui", 11, 'bold'))
  new_password_label.place(x=40, y=150)

  # ======= Update password Button ============
  update_pass = Button(win,
                       fg='#f8f8f8',
                       text='Update Password',
                       bg='#1D90F5',
                       font=("yu gothic ui", 12, "bold"),
                       command=password_change,
                       relief="flat",
                       bd=0,
                       highlightthickness=0,
                       activebackground="#1D90F5")
  update_pass.place(x=40, y=260, width=256, height=45)

def invalid():
  global win
  win.destroy()
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

def password_change():
  username_info = username.get()
  password_info = password.get()

  if password_info == "":
    invalid()
    
  elif username_info in os.listdir('login_info'):
    newpassword = cipher_suite.encrypt(bytes(password_info, encoding='utf-8'))
    with open(f"login_info/{username_info}/password", 'wb') as file:
      file.write(newpassword)

    change_success()

  else:
    username_not_found()

def change_success():
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

  win.title('Doge Password Changed')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Password changed ==================

  invalid_label = Label(win,
                        text='Password changed.',
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


def username_not_found():
  global win
  win.destroy()
  win = Toplevel()
  window_width = 350
  window_height = 250
  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()
  position_top = int(screen_height / 4 - window_height / 4)
  position_right = int(screen_width / 2 - window_width / 2)
  win.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')

  win.title('Doge User Missing')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Username not found ==================

  invalid_label = Label(win,
                        text='User not found.',
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



# ==================== DOG WALKER INVOICE PROGRAM ====================


# ==================== DOG WALKER INVOICE PROGRAM TEXT ====================

Login_headerText_image_left = PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label1 = Label(bg_imageLogin,
                                      image=Login_headerText_image_left,
                                      bg="#272A37")
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(bg_imageLogin,
                          text="Dog Walker Invoice Program™",
                          fg="#FFFFFF",
                          font=("yu gothic ui bold", 20 * -1),
                          bg="#272A37")
Login_headerText1.place(x=110, y=45)

# ==================== FROM THE CREATORS OF CALC.EXE TEXT ====================

Login_headerText_image_right = PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label2 = Label(bg_imageLogin,
                                      image=Login_headerText_image_right,
                                      bg="#272A37")
Login_headerText_image_label2.place(x=430, y=45)

Login_headerText2 = Label(bg_imageLogin,
                          anchor="nw",
                          text="From the creators™ of CALC.EXE™",
                          fg="#FFFFFF",
                          font=("yu gothic ui Bold", 20 * -1),
                          bg="#272A37")
Login_headerText2.place(x=480, y=45)

# ==================== LOGIN TO CONTINUE TEXT ====================

loginAccount_header = Label(bg_imageLogin,
                            text="Login to continue",
                            fg="#FFFFFF",
                            font=("yu gothic ui Bold", 28 * -1),
                            bg="#272A37")
loginAccount_header.place(x=75, y=121)

# ==================== NOT A MEMBER TEXT ====================

loginText = Label(bg_imageLogin,
                  text="Not a member?",
                  fg="#FFFFFF",
                  font=("yu gothic ui Regular", 15 * -1),
                  bg="#272A37")
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================

switchSignup = Button(
  bg_imageLogin,
  text="Sign Up",
  fg="#206DB4",
  font=("yu gothic ui Bold", 15 * -1),
  bg="#272A37",
  bd=0,
  #cursor="hand2",
  activebackground="#272A37",
  activeforeground="#ffffff",
  highlightthickness=0,
  pady=0,
  command=register)
switchSignup.place(x=220, y=182, width=70, height=35)

# ================ USERNAME INPUT ====================

Login_userName_image = PhotoImage(file="assets/username.png")
Login_userName_image_Label = Label(bg_imageLogin,
                                   image=Login_userName_image,
                                   bg="#272A37")
Login_userName_image_Label.place(x=76, y=242)

Login_userName_text = Label(Login_userName_image_Label,
                            text="Username",
                            fg="#FFFFFF",
                            font=("yu gothic ui SemiBold", 13 * -1),
                            bg="#3D404B")
Login_userName_text.place(x=25, y=0)

Login_userName_icon = PhotoImage(file="assets/name_icon.png")
Login_userName_icon_Label = Label(Login_userName_image_Label,
                                  image=Login_userName_icon,
                                  bg="#3D404B")
Login_userName_icon_Label.place(x=370, y=15)

Login_userName_entry = Entry(
  Login_userName_image_Label,
  bd=0,
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  font=("yu gothic ui SemiBold", 16 * -1),
)
Login_userName_entry.place(x=10, y=17, width=354, height=27)
Login_userName_entry.config(highlightbackground="#3D404B",
                            highlightcolor="#206DB4",
                            textvariable=username_login_entry)

# ================ Password Name Section ====================




Login_passwordName_image = PhotoImage(file="assets/username.png")
Login_passwordName_image_Label = Label(bg_imageLogin,
                                       image=Login_passwordName_image,
                                       bg="#272A37")
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(Login_passwordName_image_Label,
                                text="Password",
                                fg="#FFFFFF",
                                font=("yu gothic ui SemiBold", 13 * -1),
                                bg="#3D404B")
Login_passwordName_text.place(x=25, y=0)


def toggle_password():
    if Login_passwordName_entry.cget('show') == '':
        Login_passwordName_entry.config(show='*')
    else:
        Login_passwordName_entry.config(show='')

password_image = PhotoImage(file="assets/pass_icon.png")
password_button = Button(Login_passwordName_image_Label,
  bg_imageLogin,
  image=password_image,
  borderwidth=0,
  bg="#3D404B",
  command=toggle_password,
  highlightthickness=0,
  relief="flat",
  activebackground="#272A37",
)
password_button.place(x=370, y=15)

Login_passwordName_entry = Entry(
  Login_passwordName_image_Label,
  bd=0,
  show="*",
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  font=("yu gothic ui SemiBold", 16 * -1),
)
Login_passwordName_entry.place(x=10, y=17, width=354, height=27)
Login_passwordName_entry.config(highlightbackground="#3D404B",
                            highlightcolor="#206DB4",
                            textvariable=password_login_entry)

# =============== SUBMIT BUTTON ====================

Login_button_image_1 = PhotoImage(file="assets/button_1.png")
Login_button_1 = Button(
  bg_imageLogin,
  image=Login_button_image_1,
  borderwidth=0,
  highlightthickness=0,
  command=login_verify,
  relief="flat",
  activebackground="#272A37",
)
Login_button_1.place(x=120, y=445, width=333, height=65)

# ================ FORGOT PASSWORD ====================

forgotPassword = Button(
  bg_imageLogin,
  text="Forgot Password",
  fg="#206DB4",
  font=("yu gothic ui Bold", 15 * -1),
  bg="#272A37",
  bd=0,
  activebackground="#272A37",
  activeforeground="#ffffff",
  highlightthickness=0,
  pady=0,
  command=lambda: forgot_password(),
)
forgotPassword.place(x=210, y=400, width=150, height=35)

# ================ CLOSE ====================

window.mainloop()