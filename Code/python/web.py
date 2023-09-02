import tkinter as tk
import webbrowser

# Function to open a web page in the default web browser
def open_web_page():
    url = entry.get()  # Get the URL from the entry field
    webbrowser.open(url)  # Open the URL in the default web browser

# Create a tkinter window
window = tk.Tk()
window.title("Simple Web Browser")

# Create an entry field for the URL
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create a "Go" button to open the web page
go_button = tk.Button(window, text="Go", command=open_web_page)
go_button.pack(pady=5)

# Create a "Quit" button to close the browser
quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack(pady=5)

# Run the tkinter main loop
window.mainloop()
