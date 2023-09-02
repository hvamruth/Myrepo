import tkinter as tk
import usb.core

def get_connected_devices():
    devices = usb.core.find(find_all=True)
    return devices

def display_connected_devices():
    devices = get_connected_devices()
    
    device_listbox.delete(0, tk.END)  # Clear the listbox
    
    for device in devices:
        device_listbox.insert(tk.END, str(device))

# Create the main window
root = tk.Tk()
root.title("Connected Devices Analyzer")

# Create and configure widgets
label = tk.Label(root, text="Connected USB Devices:")
label.pack()

device_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
device_listbox.pack()

refresh_button = tk.Button(root, text="Refresh", command=display_connected_devices)
refresh_button.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

# Initial device list update
display_connected_devices()

# Start the GUI event loop
root.mainloop()
