import os
import socketserver
from ftplib import FTPHandler, FTPServer

# Define the FTPHandler to handle FTP commands
class MyFTPHandler(FTPHandler):
    def on_connect(self):
        print(f"Connection established from {self.remote_ip}")

    def on_disconnect(self):
        print(f"Connection closed from {self.remote_ip}")

    def on_file_sent(self, file):
        print(f"{file} sent successfully to {self.remote_ip}")

    def on_file_received(self, file):
        print(f"{file} received successfully from {self.remote_ip}")

# Define the FTP server address and port
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 2121

# Create the FTP server
server = FTPServer((HOST, PORT), MyFTPHandler)

# Set the root directory for the server (the directory you want to host)
# Make sure this path exists and contains the files you want to share
server.authorizer.add_anonymous(os.getcwd())

# Start the server
print(f"FTP Server running on {HOST}:{PORT}")
server.serve_forever()
