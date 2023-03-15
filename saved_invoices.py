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

square_left1 = PhotoImage(file="assets/square.png")
square_label11 = Label(bg_imageLogin, image=square_left, bg="#272A37")
square_label11.place(x=50, y=120)

Login_headerText1 = Label(bg_imageLogin,
                          text="Dog Walker Invoice",
                          fg="#FFFFFF",
                          font=("yu gothic ui bold", 20 * -1),
                          bg="#3d404b")
Login_headerText1.place(x=500, y=130)

delete_button_image_1 = PhotoImage(file="assets/delete_button.png")
delete_button_1 = Button(bg_imageLogin,
                        image=delete_button_image_1,
                        borderwidth=0,
                        highlightthickness=0,
                        relief="flat",
                        activebackground="#3D404B",
                        bg="#3D404B",
                        bd=0,
                        #command=delet4
                        )
delete_button_1.place(x=470, y=470)



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




def next():
    os.system('python invoice_calculator.py')

next_button_image_1 = PhotoImage(file="assets/download2.png")
next_button_1 = Button(bg_imageLogin,
                        image=next_button_image_1,
                        borderwidth=0,
                        highlightthickness=0,
                        relief="flat",
                        activebackground="#1d90f5",
                        bg="#1d90f5",
                        bd=0,
                        command=next
                        #cursor="hand2",
                        )
next_button_1.place(x=920, y=40)


window.resizable(False, False)
window.mainloop()
