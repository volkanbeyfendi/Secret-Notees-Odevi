import tkinter
from tkinter import messagebox
import base64

#pencere
my_window = tkinter.Tk()
my_window.title("Secret Notes")
my_window.config(bg="white")
#my_window.minsize(300,500)

#fotoğrafEkleme
my_image = tkinter.PhotoImage(file="topSecret.png")
#labellar
my_image_label = tkinter.Label(my_window, image=my_image, height=150, width=150)
my_image_label.grid(row=1)

my_title_label = tkinter.Label(text="Enter your title")
my_title_label.grid(row=2)

my_secret_label = tkinter.Label(text="Enter your secret")
my_secret_label.grid(row=4)

my_masterKey_label = tkinter.Label(text="Enter MASTER key")
my_masterKey_label.grid(row=6)

#entryler
my_title_entry = tkinter.Entry()
my_title_entry.grid(row=3)

my_masterKey_entry = tkinter.Entry()
my_masterKey_entry.grid(row=7)

#text
my_secret_text = tkinter.Text()
my_secret_text.config(height=10, width=30, pady=5, padx=5)
my_secret_text.grid(row=5)

def encode_questioning():
    if my_title_entry.get() == "" or my_masterKey_entry.get() == "" or my_secret_text.get("1.0",tkinter.END) == "" :
        messagebox.showerror('Error', 'Please fill all of your information')
    else :
        my_encoded_text = encode(my_masterKey_entry.get(), my_secret_text.get(1.0, tkinter.END))
        with open("secret.txt", mode="a") as saved_pass:
            saved_pass.write(f"\n[{my_title_entry.get()},{my_encoded_text}]")
        my_title_entry.delete(0 , tkinter.END)
        my_secret_text.delete(1.0, tkinter.END)
        my_masterKey_entry.delete(0 , tkinter.END)
def decode_questioning():
    if my_masterKey_entry.get() == "" or my_secret_text.get("1.0",tkinter.END) == "" :
        messagebox.showerror('Error', 'Please fill all of your information')
    else :
        my_decoded_text = decode(my_masterKey_entry.get(), my_secret_text.get("1.0",tkinter.END))
        my_secret_text.delete(1.0, tkinter.END)
        my_masterKey_entry.delete(0, tkinter.END)
        my_secret_text.insert("end", my_decoded_text)

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#butonlar
my_saveencrypt_button = tkinter.Button(text="Save&Encrypt", command=encode_questioning)
my_saveencrypt_button.grid(row=8)

my_decrypt_button = tkinter.Button(text="Decrypt", command=decode_questioning)
my_decrypt_button.grid(row=9)

my_window.mainloop()