import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        # Create frames
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(fill="x")

        self.password_frame = tk.Frame(self.root)
        self.password_frame.pack(fill="x")

        # Create options
        self.length_label = tk.Label(self.options_frame, text="Password Length:")
        self.length_label.pack(side="left")

        self.length_entry = tk.Entry(self.options_frame, width=5)
        self.length_entry.pack(side="left")

        self.use_uppercase = tk.BooleanVar()
        self.use_uppercase.set(True)
        self.uppercase_checkbox = tk.Checkbutton(self.options_frame, text="Uppercase", variable=self.use_uppercase)
        self.uppercase_checkbox.pack(side="left")

        self.use_lowercase = tk.BooleanVar()
        self.use_lowercase.set(True)
        self.lowercase_checkbox = tk.Checkbutton(self.options_frame, text="Lowercase", variable=self.use_lowercase)
        self.lowercase_checkbox.pack(side="left")

        self.use_numbers = tk.BooleanVar()
        self.use_numbers.set(True)
        self.numbers_checkbox = tk.Checkbutton(self.options_frame, text="Numbers", variable=self.use_numbers)
        self.numbers_checkbox.pack(side="left")

        self.use_symbols = tk.BooleanVar()
        self.use_symbols.set(True)
        self.symbols_checkbox = tk.Checkbutton(self.options_frame, text="Symbols", variable=self.use_symbols)
        self.symbols_checkbox.pack(side="left")

        self.exclude_similar = tk.BooleanVar()
        self.exclude_similar.set(False)
        self.exclude_similar_checkbox = tk.Checkbutton(self.options_frame, text="Exclude similar characters", variable=self.exclude_similar)
        self.exclude_similar_checkbox.pack(side="left")

        # Create password display
        self.password_label = tk.Label(self.password_frame, text="Generated Password:")
        self.password_label.pack(side="left")

        self.password_entry = tk.Entry(self.password_frame, width=40)
        self.password_entry.pack(side="left")

        self.copy_button = tk.Button(self.password_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(side="left")

        self.generate_button = tk.Button(self.options_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(side="left")

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8 characters")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length")
            return

        characters = ""
        if self.use_uppercase.get():
            characters += string.ascii_uppercase
        if self.use_lowercase.get():
            characters += string.ascii_lowercase
        if self.use_numbers.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += string.punctuation

        if self.exclude_similar.get():
            characters = characters.replace('l', '').replace('I', '').replace('1', '')
            characters = characters.replace('o', '').replace('O', '').replace('0', '')
            characters = characters.replace('s', '').replace('S', '').replace('5', '')

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()