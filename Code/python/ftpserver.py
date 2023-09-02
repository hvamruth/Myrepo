import ftplib
import tkinter as tk
from tkinter import messagebox

def list_files():
    try:
        ftp = ftplib.FTP(server_entry.get(), user_entry.get(), password_entry.get())
        ftp.cwd(directory_entry.get())

        files = ftp.nlst()
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)

        ftp.quit()
    except ftplib.all_errors as e:
        messagebox.showerror("Error", f"Error listing files: {e}")

# GUI Setup
root = tk.Tk()
root.title("FTP Server")
root.geometry("400x300")

server_label = tk.Label(root, text="Server:")
server_label.pack(pady=10)

server_entry = tk.Entry(root)
server_entry.pack(pady=5)

user_label = tk.Label(root, text="Username:")
user_label.pack(pady=5)

user_entry = tk.Entry(root)
user_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

directory_label = tk.Label(root, text="Directory:")
directory_label.pack(pady=5)

directory_entry = tk.Entry(root)
directory_entry.pack(pady=5)

list_button = tk.Button(root, text="List Files", command=list_files)
list_button.pack(pady=10)

file_list = tk.Listbox(root)
file_list.pack(pady=5, fill=tk.BOTH, expand=True)

root.mainloop()
