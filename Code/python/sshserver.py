import paramiko
import threading
import tkinter as tk
from tkinter import messagebox

class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        # Here, you can implement your custom logic for user authentication.
        # For simplicity, we'll allow any username and password combination.
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return 'password'

def start_ssh_server():
    host_key = paramiko.RSAKey.generate(2048)
    ssh_server = paramiko.Transport(('0.0.0.0', 22))
    ssh_server.add_server_key(host_key)

    ssh_server.set_subsystem_handler('sftp', paramiko.SFTPServer, {})
    ssh_server.start_server(server=SSHServer())

    print("SSH Server started.")

    while True:
        client, addr = ssh_server.accept(20)
        if client is None:
            continue

        t = paramiko.Transport(client)
        t.load_server_moduli()
        t.add_server_key(host_key)

        server = SSHServer()
        t.start_server(server=server)

def on_start_server():
    try:
        start_thread = threading.Thread(target=start_ssh_server)
        start_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"Error starting SSH server: {e}")

def on_stop_server():
    # You can add proper shutdown logic here if needed.
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("SSH Server")
root.geometry("300x150")

start_button = tk.Button(root, text="Start Server", command=on_start_server)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Server", command=on_stop_server, state=tk.DISABLED)
stop_button.pack(pady=20)

root.mainloop()
