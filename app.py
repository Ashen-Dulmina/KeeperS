from textwrap import fill
import customtkinter as ctk #for GUI
import webbrowser #for giving credits and sourcing themes
import json #for line 209
from cryptography.fernet import Fernet #to encrypt and decrypt
from CTkMessagebox import CTkMessagebox #for error messages and other
from PIL import Image #for GUI icons
from tkinter import Scrollbar, filedialog as fd #for getting file paths

#define themes
ctk.set_appearance_mode("Dark") #set default theme to dark
ctk.set_default_color_theme("themes/violet.json") #set color scheme to violet (Change later)

# window
root = ctk.CTk() #defines root
root.resizable(False, False) #disables resizing
root.title("KeeperS | Encryptor And Decryptor 1.0v") #sets title
root.geometry("560x320") #sets window size
root.iconbitmap("icons/app.ico") #sets app icon

#functions
#generate new key
def generate_new_key():
  filename = fd.asksaveasfilename(defaultextension=".key",  filetypes=[("Encryption Keys", "*.key")]) #geth the new files name and location to be saved
  if filename: #if the file is selected
    try:
      key = Fernet.generate_key() #generate a new key
      with open(filename, 'wb') as file: #opens the newly made file in writing mode
        file.write(key) #writed the key to it
    except:
      msg = CTkMessagebox(title = "Error !",
                          message = "An Unexpected Error Occured While Writing The Key File",
                          icon = "error",
                          option_1 = "Ok") #gives this error message if it fails

#select key
def get_existing_key(file):
  format_file = open(file, 'rb') #opens the key file from args in reading mode
  final_key = format_file.read() #reads the file
  return final_key #returns the key to the caller

#encrypt text
def encrypt_text(key, text):
  enc_key = Fernet(key) #gets the encryption key from args
  enc_text = enc_key.encrypt(text) #encrypts the text
  return enc_text #returns the text to caller

#decrypt text
def decrypt_text(key, text):
  dec_key = Fernet(key) #gets the encryption key from args
  dec_text = dec_key.decrypt(text) #decrypts the text
  return dec_text #returnd the text to caller

#encrypt files
def encrypt_files(key, file):
  enc_key = Fernet(key) #gets the encryption keys from function argumants
  output_file = fd.asksaveasfilename(defaultextension=".*",  filetypes=[("All Files", "*.*")]) #gets the output file
  
  with open(file, 'rb') as to_enc_file: #opens the original file in read bits mode
    original = to_enc_file.read() #reads the file
  
  encrypted = enc_key.encrypt(original) #encrypt the file
  
  with open(output_file, 'wb') as encrypted_file: #opens the output file in writing mode
    encrypted_file.write(encrypted) #rites the data
  
#decrypt files
def decrypt_files(key, file):
  dec_key = Fernet(key) #gets the decryption key from argumants
  output_file = fd.asksaveasfilename(defaultextension=".*", filetypes=[("All Files", "*.*")]) #gets the output file
  
  with open(file, 'rb') as enc_file: #opens the encrypted file in reading mode
    encrypted = enc_file.read() #reads the encrypted file
    
  decrypted = dec_key.decrypt(encrypted) #decrypt the file
  
  with open(output_file, 'wb') as dec_file: #opens the output file in writing mode
    dec_file.write(decrypted) #writes the file


#gui

#sidenav
side_nav = ctk.CTkFrame(root, corner_radius=0) #creates side navbar
side_nav.grid(row=0, column=0, sticky="nsew") #makes it a grid
side_nav.grid_rowconfigure(4, weight=1) #configures it

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
	command=lambda :webbrowser.open_new_tab("https://github.com/Ashen-Dulmina") #takes users to my github page  # type: ignore
)

#the below part assigns the buttons in their corresponding place
key_genaratr_btn_sidebar.grid(row=0, column=0, sticky="ew")
text_encrypt_btn_sidebar.grid(row=1, column=0, sticky="ew")
file_encrypt_btn_sidebar.grid(row=2, column=0, sticky="ew")
text_decrypt_btn_sidebar.grid(row=3, column=0, sticky="ew")
file_decrypt_btn_sidebar.grid(row=4, column=0, sticky="ew")
settings_btn_sidebar.grid(row=5, column=0, sticky="ew")
guide_btn_sidebar.grid(row=6, column=0, sticky="ew")
blank_btn_sidebar.grid(row=7, column=0, sticky="ew")
creditz_btn_sidebar.grid(row=8, column=0, sticky="ew") 

#frames 

#key generator framee
key_gen_frame = ctk.CTkFrame(root,  corner_radius=0, fg_color="transparent") #makes the frame
lable_one = ctk.CTkLabel(key_gen_frame, text="Generate An Encryption Key", font=("Consolas bold", 18)) #make a text label # under:key_gen_frame
generate_key_button = ctk.CTkButton(key_gen_frame, height=30, width=200, text="Generate A New Key") #make a button # under:key_gen_frame
lable_two = ctk.CTkLabel(key_gen_frame, text="Existing Encryption Keys", font=("Consolas bold", 18)) #make another text label # under:key_gen_frame
#make an embedded json list and a table to list out keys


#key_gen_frame.grid(row=0, column=1, sticky="nsew") #align key_gen_frame
lable_one.pack(padx=10, pady=5, anchor=ctk.W) #pack label one
generate_key_button.pack(padx=60, pady=8) #pack the button
lable_two.pack(padx=10, pady=(17,5), anchor=ctk.W) #pack label two

#encrypt text frem
encrypt_text_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent") #makes a frame
scrollbar_encrypt_text_frame = ctk.CTkScrollbar(encrypt_text_frame) #define scrollbar
lable_three = ctk.CTkLabel(encrypt_text_frame, text="Encrypt Text", font=("Consolas bold", 18)) #make a text label # under: encrypt_text_frame
label_four = ctk.CTkLabel(encrypt_text_frame, text="Select Key :-", font=("Arial", 12)) #make a text label # under: encrypt_text_frame
frame_in_encrypt_text_frame = ctk.CTkFrame(encrypt_text_frame, corner_radius=0, fg_color="transparent") #makes a frame
keys_path_enc_txt_entry = ctk.CTkEntry(frame_in_encrypt_text_frame, width=300, height=30, placeholder_text="Key File Path") #key file entry
browse_icon = ctk.CTkImage(Image.open("icons/browse.png")) #browse files icon
browse_key_enc_txt_button = ctk.CTkButton(frame_in_encrypt_text_frame, width=30, height=30, image=browse_icon, text="") # add the browse files button
label_five = ctk.CTkLabel(encrypt_text_frame, text="Text To Encrypt :-", font=("Arial", 12)) #make a text label
text_to_encrypt_textbox = ctk.CTkTextbox(encrypt_text_frame, width=330, height=70, border_width=2, corner_radius=10) #make a textbox
label_six = ctk.CTkLabel(encrypt_text_frame, text="Encrypted Text :-", font=("Arial", 12)) #make text label
encrypted_text_textbox = ctk.CTkTextbox(encrypt_text_frame, width=330, height=70, border_width=2, corner_radius=10) #make a textbox
encrypt_text_button = ctk.CTkButton(encrypt_text_frame, text="Encrypt Text") #make the encrypt button

encrypt_text_frame.grid(row=0, column=1, sticky="nsew") #align encrypt_text_frame
scrollbar_encrypt_text_frame.pack(side=ctk.RIGHT, fill=ctk.Y)
lable_three.pack(padx=10, pady=5, anchor=ctk.W) #pack label 3
label_four.pack(padx=10, pady=(10,5), anchor=ctk.W) #pack label 4
frame_in_encrypt_text_frame.pack(padx=10, pady=(0,5)) #pack frame
keys_path_enc_txt_entry.pack(side=ctk.LEFT, padx=10, pady=(0,5)) #pack entry
browse_key_enc_txt_button.pack(side=ctk.LEFT) #pack browse button
label_five.pack(padx=5, anchor=ctk.W) #pack lable 5
text_to_encrypt_textbox.pack(padx=5, pady=5) #pack textbox
label_six.pack(padx=5, pady=(5,0), anchor=ctk.W) #pack label 6
encrypted_text_textbox.pack(padx=5, pady=5) #pack textbox
encrypt_text_button.pack(padx=5, pady=5) #pack encrypt button


# window display
root.mainloop()