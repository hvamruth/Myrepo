import tkinter as tk
import webbrowser

# Function to perform the web search
def perform_search():
    query = entry.get()  # Get the search query from the entry field
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)  # Open the default web browser with the search results

# Create a tkinter window
window = tk.Tk()
window.title("Advanced HTML Search Engine")

# Create a label
label = tk.Label(window, text="Enter your search query:")
label.pack(pady=10)

# Create an entry field for the search query
entry = tk.Entry(window, width=40)
entry.pack()

# Create a search button
search_button = tk.Button(window, text="Search", command=perform_search)
search_button.pack(pady=10)

# Run the tkinter main loop
window.mainloop()
