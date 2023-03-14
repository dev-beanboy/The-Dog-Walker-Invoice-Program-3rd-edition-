# ==================== MODULES ====================

import os
import shutil
from tkinter import *

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
global attempts
username_verify = StringVar()
password_verify = StringVar()

# ==================== SUBROUTINES ====================

def register():
  os.system('python register_page.py')


def end():
  win.destroy()
def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_login_entry.delete(0, END)
  password_login_entry.delete(0, END)

  list_of_files = os.listdir("login_info")
  if username1 in list_of_files:
    file1 = open(f"login_info/{username1}", "r")
    verify = file1.read().split()
    if password1 in verify:
      login_sucess()
    else:
      password_not_recognised()
  else:
    user_not_found()

def login_sucess():
  global login_success_screen
  attempts = 5
  login_success_screen = Toplevel(login_screen)
  login_success_screen.title("Doge Success")
  login_success_screen.geometry("300x300")
  login_success_screen.configure(bg='white')
  login_success_screen.resizable(width=False, height=False)
  Label(login_success_screen, text="", bg="white").pack()
  Label(login_success_screen, text="Login Success", bg="white").pack()
  Label(login_success_screen, text="", bg="white").pack()
  Button(login_success_screen,
         text="Run program",
         height="2",
         width="18",
         bg="skyblue",
         fg="white",
         highlightthickness=0,
         pady=0,
         bd=0,
         font=("Calibri", 9),
         command=delete_login_success).pack()

def password_not_recognised():
  global password_not_recog_screen
  password_not_recog_screen = Toplevel(login_screen)
  password_not_recog_screen.title("Doge not found")
  password_not_recog_screen.geometry("150x100")
  pasword_not_recog_screen.configure(bg='white')
  password_not_recog_screen.resizable(width=False, height=False)
  Label(password_not_recog_screen, text="Invalid Password ").pack()
  Button(password_not_recog_screen,
         text="OK",
         height="2",
         width="18",
         bg="skyblue",
         fg="white",
         highlightthickness=0,
         pady=0,
         bd=0,
         font=("Calibri", 9),
         command=delete_password_not_recognised).pack()


def user_not_found():
  global user_not_found_screen
  user_not_found_screen = Toplevel(login_screen)
  user_not_found_screen.title(" Doge Failure")
  user_not_found_screen.geometry("150x100")
  user_not_found_screen.configure(bg='white')
  user_not_found_screen.resizable(width=False, height=False)
  Label(user_not_found_screen, text="User Not Found").pack()
  Button(user_not_found_screen,
         text="OK",
         height="2",
         width="18",
         bg="skyblue",
         fg="white",
         highlightthickness=0,
         pady=0,
         bd=0,
         font=("Calibri", 9),
         command=delete_user_not_found_screen).pack()

def delete_login_success():
  login_success_screen.destroy()
  os.system('invoice_calculator.py')
  window.destroy()


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
  #win.iconbitmap('assets/headerText_image.png')
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
                       command=passwordchange,
                       relief="flat",
                       bd=0,
                       highlightthickness=0,
                       activebackground="#1D90F5")
  update_pass.place(x=40, y=260, width=256, height=45)


def passwordchange():
  username_info = username.get()
  password_info = password.get()

  if username_info in os.listdir('login_info'):
    with open(f"login_info/{username_info}/{username_info}", 'r') as file:
      data = file.readlines()

    data[3] = password_info

    with open(f"login_info/{username_info}/{username_info}", 'w') as file:
      file.writelines(data)

    change_success()

  else:
    username_not_found()

def change_success():
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

  win.title('Doge Account Missing')
  win.configure(background='#272A37')
  win.resizable(False, False)

  # ====  Username not found ==================

  invalid_label = Label(win,
                        text='Account not found.',
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

Login_passwordName_icon = PhotoImage(file="assets/pass_icon.png")
Login_passwordName_icon_Label = Label(Login_passwordName_image_Label,
                                      image=Login_passwordName_icon,
                                      bg="#3D404B")
Login_passwordName_icon_Label.place(x=370, y=15)

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