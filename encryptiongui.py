import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Encrypt Function
def encrypt():
    text = message_entry.get()

    try:
        shift = int(shift_entry.get())
    except:
        result_label.configure(text="Please enter a valid shift key!")
        return

    encrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    result_label.configure(
        text=f"Encrypted Text:\n{encrypted}"
    )


# Decrypt Function
def decrypt():
    text = message_entry.get()

    try:
        shift = int(shift_entry.get())
    except:
        result_label.configure(text="Please enter a valid shift key!")
        return

    decrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted += char

    result_label.configure(
        text=f"Decrypted Text:\n{decrypted}"
    )


# Clear Function
def clear():
    message_entry.delete(0, "end")
    shift_entry.delete(0, "end")
    result_label.configure(text="")


# Main Window
app = ctk.CTk()
app.title("Caesar Cipher Tool")
app.geometry("700x500")

title = ctk.CTkLabel(
    app,
    text="🔐 Caesar Cipher Encryption & Decryption",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

# Message Input
message_entry = ctk.CTkEntry(
    app,
    width=500,
    height=40,
    placeholder_text="Enter Message"
)
message_entry.pack(pady=15)

# Shift Key Input
shift_entry = ctk.CTkEntry(
    app,
    width=200,
    height=40,
    placeholder_text="Enter Shift Key"
)
shift_entry.pack(pady=10)

# Buttons Frame
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="Encrypt",
    command=encrypt
)
encrypt_btn.pack(side="left", padx=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="Decrypt",
    command=decrypt
)
decrypt_btn.pack(side="left", padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="Clear",
    command=clear
)
clear_btn.pack(side="left", padx=10)

# Result Area
result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 18)
)
result_label.pack(pady=30)

footer = ctk.CTkLabel(
    app,
    text="DecodeLabs Project 2 - Basic Encryption & Decryption"
)
footer.pack(side="bottom", pady=15)

app.mainloop()