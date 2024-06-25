import cryptography
from cryptography.fernet import Fernet
import customtkinter as ctk
from PIL import Image
import webbrowser  
import tkinter as tk
from tkinter import filedialog as fd 

#define themes
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("themes/violet.json")

# window
root = ctk.CTk()
root.resizable(False, False)
root.title("KeeperS | Encryptor And Decryptor 1.0v")
root.geometry("500x320")
root.iconbitmap("icons/app.ico")

#functions
def get_existing_key():
	selected_file = fd.askopenfilename()

#gui

#sidenav
side_nav = ctk.CTkFrame(root, corner_radius=0)
side_nav.grid(row=0, column=0, sticky="nsew")
side_nav.grid_rowconfigure(4, weight=1)

#sidenav.components
#key generator
key_genaratr_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Key Generator",
	fg_color="transparent",
	anchor="w")

#encrypt text srings
text_encrypt_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Encrypt Text",
	fg_color="transparent",
	anchor="w")

#encrypt files
file_encrypt_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Encrypt Files",
	fg_color="transparent",
	anchor="w")

#decrypt text srings
text_decrypt_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Decrypt Text",
	fg_color="transparent",
	anchor="w")

#decrypt files
file_decrypt_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Decrypt Files",
	fg_color="transparent",
	anchor="w")

#settings
settings_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "Settings",
	fg_color="transparent",
	anchor="w")

#guide
guide_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "User Guide",
	fg_color="transparent",
	anchor="w")

#blank spacer
blank_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	text = "",
	fg_color="transparent",
	anchor="w")

#credits
creditz_icon = ctk.CTkImage(Image.open("icons/github.png"))
creditz_btn_sidebar = ctk.CTkButton(
	side_nav,
	corner_radius = 0,
	height = 25,
	width = 30,
	border_spacing = 10,
	image = creditz_icon,
	text = "Made by Ashen Dulmina",
	font=("Arial", 10),
	fg_color="transparent",
	anchor="w",
	command=lambda :webbrowser.open_new_tab("https://github.com/Ashen-Dulmina"))

key_genaratr_btn_sidebar.grid(row=0, column=0, sticky="ew")
text_encrypt_btn_sidebar.grid(row=1, column=0, sticky="ew")
file_encrypt_btn_sidebar.grid(row=2, column=0, sticky="ew")
text_decrypt_btn_sidebar.grid(row=3, column=0, sticky="ew")
file_decrypt_btn_sidebar.grid(row=4, column=0, sticky="ew")
settings_btn_sidebar.grid(row=5, column=0, sticky="ew")
guide_btn_sidebar.grid(row=6, column=0, sticky="ew")
blank_btn_sidebar.grid(row=7, column=0, sticky="ew")
creditz_btn_sidebar.grid(row=8, column=0, sticky="ew")

# window display
root.mainloop()