import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get("1.0", tk.END))  # Get the length from the Text widget
    if length > 0:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_result.delete("1.0", tk.END)  # Clear previous result
        password_result.insert(tk.END, password)

def accept_password():
    generated_password = password_result.get("1.0", tk.END).strip()
    if generated_password:
        pyperclip.copy(generated_password)
        print("Copied to clipboard:", generated_password)

def reset_password():
    password_result.delete("1.0", tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("530x400")

# Heading with underline
heading_label = tk.Label(root, text="Password Generator", font = ("Poppins", 20, "underline", "bold"))
heading_label.pack(pady=5)
blank_label = tk.Label(root, text="")
blank_label.pack()
blank_label = tk.Label(root, text="")
blank_label.pack()

# Frame to hold the label and entry box
input_frame = tk.Frame(root)
input_frame.pack()

# Label for entering password length
length_label = tk.Label(input_frame, text="Enter password length :", font = ("Poppins", 12))
length_label.pack(side="left", padx=12, pady=12)

# Text widget for entering password length
length_entry = tk.Text(input_frame, height=1, width=20, borderwidth=3, relief="ridge")
length_entry.pack(side="left")

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", font = ("Poppins", 12, "bold"), command=generate_password, bg="blue",fg="white")
generate_button.pack(pady=5)
generate_label = tk.Label(root, text="Generated password :", font = ("Poppins", 12))
generate_label.pack(pady=10)

# Text widget to display the generated password
password_result = tk.Text(root, height=1, width=45, borderwidth=3, relief="ridge")
password_result.pack(pady=10)

# Button to accept the generated password and copy to clipboard
accept_button = tk.Button(root, text="Accept Password", font = ("Poppins", 12, "bold"), command=accept_password, bg="green",fg="white")
accept_button.pack(pady=5)

# Button to reset the generated password
reset_button = tk.Button(root, text="Reset Password",font = ("Poppins", 12, "bold"), command=reset_password, bg="red",fg="white")
reset_button.pack(pady=5)

root.mainloop()