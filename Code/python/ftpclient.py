import ftplib
import tkinter as tk
from tkinter import filedialog, messagebox

def upload_file():
    try:
        ftp = ftplib.FTP(server_entry.get(), user_entry.get(), password_entry.get())
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = file_path.split("/")[-1]
            with open(file_path, 'rb') as file:
                ftp.storbinary(f"STOR {file_name}", file)
                messagebox.showinfo("Success", f"File '{file_name}' uploaded successfully.")

        ftp.quit()
    except ftplib.all_errors as e:
        messagebox.showerror("Error", f"Error uploading file: {e}")

# GUI Setup
root = tk.Tk()
root.title("FTP Client")
root.geometry("400x200")

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

upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(pady=10)

root.mainloop()
