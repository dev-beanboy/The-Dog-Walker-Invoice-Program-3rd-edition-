# ================ IMPORTS ====================
import os
import shutil
from tkinter import *
import time

# ================ MAIN WINDOW ====================
window = Tk()
window.title("Doge Walker Invoice Program")
height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

global days_entry
global dogs_entry

days_entry = 0
dogs_entry = 0

window.configure(bg="#525561")


def open():
  os.system('python register_page.py')


# ================Background Image ====================

backgroundImage = PhotoImage(file="assets/image_1.png")
bg_image = Label(window, image=backgroundImage, bg="#525561")
bg_image.place(x=120, y=28)

Login_backgroundImage = PhotoImage(file="assets/image_1.png")
bg_imageLogin = Label(window, image=Login_backgroundImage, bg="#525561")
bg_imageLogin.place(x=120, y=28)

# ================ Header Text Left ====================

Login_headerText_image_left = PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label1 = Label(bg_imageLogin,
                                      image=Login_headerText_image_left,
                                      bg="#272A37")
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(bg_imageLogin,
                          text="Dog Walker Inoice Program™",
                          fg="#FFFFFF",
                          font=("yu gothic ui bold", 20 * -1),
                          bg="#272A37")
Login_headerText1.place(x=110, y=45)


# ================ Header Text Right ====================

Login_headerText_image_right = PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label2 = Label(bg_imageLogin,
                                      image=Login_headerText_image_right,
                                      bg="#272A37")
Login_headerText_image_label2.place(x=430, y=45)

Login_headerText2 = Label(bg_imageLogin,
                          anchor="nw",
                          text="From the creators of CALC.EXE™",
                          fg="#FFFFFF",
                          font=("yu gothic ui Bold", 20 * -1),
                          bg="#272A37")
Login_headerText2.place(x=480, y=45)

# ================ Enter Dog Text====================
loginAccount_header = Label(bg_imageLogin,
                            text="Enter Dog Walking Data",
                            fg="#FFFFFF",
                            font=("yu gothic ui Bold", 28 * -1),
                            bg="#272A37")
loginAccount_header.place(x=75, y=121)

# ================ Dog Walker Invoice Shape ====================
square_left = PhotoImage(file="assets/square.png")
square_label1 = Label(bg_imageLogin, image=square_left, bg="#272A37")
square_label1.place(x=450, y=120)

Login_headerText1 = Label(bg_imageLogin,
                          text="Dog Walker Invoice",
                          fg="#FFFFFF",
                          font=("yu gothic ui bold", 20 * -1),
                          bg="#3d404b")
Login_headerText1.place(x=500, y=130)

# ================ Invoice Placeholder Text ====================

sum = 0

label16 = Label(bg_imageLogin,
                text="Total Walks: " + str(sum),
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#3d404b")
label16.place(x=470, y=340)

label17 = Label(bg_imageLogin,
                text="Total Dogs: " + str(sum),
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#3d404b")
label17.place(x=470, y=280)

label18 = Label(bg_imageLogin,
                text="Total Days: " + str(sum),
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#3d404b")
label18.place(x=470, y=220)

label19 = Label(bg_imageLogin,
                text="Invoice: £" + str(sum),
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#3d404b")
label19.place(x=470, y=400)

# ================ All Calculations ====================


def calculate():
  global label16
  global label17
  global label18
  global label19

  label16.destroy()
  label17.destroy()
  label18.destroy()
  label19.destroy()

  sum = 0
  sum2 = 0
  
  if dogs_entry.get() != "":
    t1 = int(dogs_entry.get())
  else:
    t1 = ""
  if days_entry.get() != "":
    t2 = int(days_entry.get())
  else:
      print("hi")

  if t1 == "" or t2 == "":
    t1 = 0
    t2 = 0

  sum = t1 * t2
  sum2 = sum * 4

  label16 = Label(bg_imageLogin,
                  text="Total Walks: " + str(sum),
                  fg="#FFFFFF",
                  font=("yu gothic ui bold", 20 * -1),
                  bg="#3d404b")
  label16.place(x=470, y=340)

  label17 = Label(bg_imageLogin,
                  text="Total Dogs: " + str(t1),
                  fg="#FFFFFF",
                  font=("yu gothic ui bold", 20 * -1),
                  bg="#3d404b")
  label17.place(x=470, y=280)

  label18 = Label(bg_imageLogin,
                  text="Total Days: " + str(t2),
                  fg="#FFFFFF",
                  font=("yu gothic ui bold", 20 * -1),
                  bg="#3d404b")
  label18.place(x=470, y=220)

  label19 = Label(bg_imageLogin,
                  text="Invoice: £" + str(sum2),
                  fg="#FFFFFF",
                  font=("yu gothic ui bold", 20 * -1),
                  bg="#3d404b")
  label19.place(x=470, y=400)


# ================ Number of Days Section ====================

days_image = PhotoImage(file="assets/username1.png")
days_Label = Label(bg_imageLogin, image=days_image, bg="#272A37")
days_Label.place(x=76, y=242)

days_text = Label(days_Label,
                  text="Number of Days",
                  fg="#FFFFFF",
                  font=("yu gothic ui SemiBold", 13 * -1),
                  bg="#3D404B")
days_text.place(x=25, y=0)

days_entry = Entry(
  days_Label,
  bd=0,
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  font=("yu gothic ui SemiBold", 16 * -1),
)
days_entry.place(x=10, y=17, width=200, height=27)

# ================ Number of Dogs Section ====================
dogs_image = PhotoImage(file="assets/username1.png")
dogs_Label = Label(bg_imageLogin, image=dogs_image, bg="#272A37")
dogs_Label.place(x=80, y=330)

dogs_text = Label(dogs_Label,
                  text="Number of Dogs",
                  fg="#FFFFFF",
                  font=("yu gothic ui SemiBold", 13 * -1),
                  bg="#3D404B")
dogs_text.place(x=25, y=0)

dogs_entry = Entry(
  dogs_Label,
  bd=0,
  fg="white",
  bg="#3D404B",
  highlightthickness=0,
  font=("yu gothic ui SemiBold", 16 * -1),
)
dogs_entry.place(x=10, y=17, width=200, height=27)

# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(file="assets/button_1.png")
Login_button_1 = Button(bg_imageLogin,
                        image=Login_button_image_1,
                        borderwidth=0,
                        highlightthickness=0,
                        relief="flat",
                        activebackground="#272A37",
                        command=calculate
                        #cursor="hand2",
                        )
Login_button_1.place(x=70, y=445, width=333, height=65)



window.resizable(False, False)
window.mainloop()
