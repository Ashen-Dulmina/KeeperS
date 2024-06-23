import cryptography 
import customtkinter as ctk
from cryptography.fernet import Fernet

#rootkit
root = ctk.CTk()
root.resizable(False,False)
root.title("Encryptor And Decryptor")

#theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")



#spegatti - geniyak
def generate_new_key():
	new_key_file_name = new_key_entry.get()
	processed_new_key_file_name = open(f"{new_key_file_name}.key",'wb')
	with processed_new_key_file_name as keyfile:
		new_key = Fernet.generate_key()
		keyfile.write(new_key)

#spegatti - getfil
def get_existing_key_from_file():
	existing_key_file = key_encr_entry.get()
	processed_existing_key_file = open(f"{existing_key_file}.key",'rb')
	readout_processed_existing_key_file = processed_existing_key_file.read()
	return readout_processed_existing_key_file

#spegatti - 404! gAAAAABmF5VMnAhq3m0m8ophwzGS2Ltj4t3yUNcJwkVOVIKgnBBNdLvWEcKe3oYL5CCFSnzqOJKdv8mfj_xbiRHATb59VHuV8Q==
def encrypt_data_using_key():
	init_data = encry_text.get("1.0",'end-1c')
	processed_init_data = init_data.encode('utf-8')
	encyption_key = get_existing_key_from_file()
	processed_encryption_key = Fernet(encyption_key)
	encrypt_final_product = processed_encryption_key.encrypt(processed_init_data)
	encrypt_final_product_string_format = encrypt_final_product.decode('utf-8')
	encry_output.insert("0.0", encrypt_final_product_string_format)
	print(encrypt_final_product_string_format)

#spegatti - 200! gAAAAABmF5dEyvyNloSiQQSnyEF8Am8huj8h2AtJuFZ31jH3gOZSgc7fzYgmwMrajb3GtbD4lYbr15oRT5X2zFA8QcZOhb6zDA==
def decrypt_data_using_key():
	cyro_data = decry_text.get("1.0",'end-1c')
	processed_cyro_data = cyro_data.encode('utf-8')
	encyption_key = get_existing_key_from_file()
	processed_encryption_key = Fernet(encyption_key)
	decrypt_final_product = processed_encryption_key.decrypt(processed_cyro_data)
	decrypt_final_product_string_format = decrypt_final_product.decode('utf-8')
	decry_output.insert("0.0", decrypt_final_product_string_format)
	print(decrypt_final_product_string_format)


#generate new kwy widgets
#label1
new_key_label = ctk.CTkLabel(root, 
												text = "Generate New Key",
												font=("Consolas bold", 18)											
)
new_key_label.pack(padx=10, pady=1, anchor=ctk.W)

#entry1
new_key_entry = ctk.CTkEntry(
															master=root,
                              placeholder_text="New Key File Name (Without extention plz)",
                              width=320,
                              height=35,
                              border_width=2,
                              corner_radius=10
)
new_key_entry.pack(padx=10, pady=3)

#ses button 1
new_key_button = ctk.CTkButton(
			master=root,
			height=30,
			width=90,
			corner_radius=35,
			text="Generate Key",
			command=generate_new_key
)
new_key_button.pack(padx=10, pady=5)

key_label = ctk.CTkLabel(root, 
												text = "Key Selection",
												font=("Consolas bold", 18)												
)
key_label.pack(padx=10, pady=2, anchor=ctk.W)

#keylabel223
key_ask_label = ctk.CTkLabel(
			root,
			text="Encryption key :",
			font=("Arial", 12)
)
key_ask_label.pack(padx=10, pady=1, anchor=ctk.W)

#smalas
key_encr_entry = ctk.CTkEntry(
										root,
										placeholder_text="Key file name (No extention plz)",
										height=35,
										width=320,
										border_width=2,
										corner_radius=10
)
key_encr_entry.pack(padx=10)

#encrypt shit
#label
encrypt_label = ctk.CTkLabel(root, 
												text = "Encrypt Shit",
												font=("Consolas bold", 18)												
)
encrypt_label.pack(padx=10, pady=2, anchor=ctk.W)

#room temp iq
text_label_for_encr = ctk.CTkLabel(
			root,
			text="Text To Encrypt :",
			font=("Arial", 12)
)
text_label_for_encr.pack(padx=10, pady=1, anchor=ctk.W)


#sortdiq
encry_text = ctk.CTkTextbox(
		root,
		height=70,
		width=320,
		border_width=2,
		corner_radius=10
)
encry_text.pack(padx=10, pady=2)

enc_out_label = ctk.CTkLabel(
			root,
			text="Encrypted Text :",
			font=("Arial", 12)
)
enc_out_label.pack(padx=10, pady=1, anchor=ctk.W)

#4q
encry_output = ctk.CTkTextbox(
		root,
		height=30,
		width=320,
		border_width=2,
		corner_radius=10
)
encry_output.pack(padx=10, pady=2)

#peniz
encry_trigger_button = ctk.CTkButton(
				root,
				text="Encrypt Text",
				height=30,
				width=90,
				corner_radius=35,
				command=encrypt_data_using_key
)
encry_trigger_button.pack(padx=10, pady=4)

#label
decrypt_label = ctk.CTkLabel(root, 
												text = "Decrypt Shit",
												font=("Consolas bold", 18)												
)
decrypt_label.pack(padx=10, pady=2, anchor=ctk.W)

#room temp iq
text_label_for_decr = ctk.CTkLabel(
			root,
			text="Text To Decrypt :",
			font=("Arial", 12)
)
text_label_for_decr.pack(padx=10, pady=1, anchor=ctk.W)

#sortdiq
decry_text = ctk.CTkTextbox(
		root,
		height=70,
		width=320,
		border_width=2,
		corner_radius=10
)
decry_text.pack(padx=10, pady=2)

dec_out_label = ctk.CTkLabel(
			root,
			text="Decrypted Text :",
			font=("Arial", 12)
)
dec_out_label.pack(padx=10, pady=1, anchor=ctk.W)

decry_output = ctk.CTkTextbox(
		root,
		height=30,
		width=320,
		border_width=2,
		corner_radius=10
)
decry_output.pack(padx=10, pady=2)

#peniz
decry_trigger_button = ctk.CTkButton(
				root,
				text="Decrypt Text",
				height=30,
				width=90,
				corner_radius=35,
				command=decrypt_data_using_key
)
decry_trigger_button.pack(padx=10, pady=4)

root.mainloop()