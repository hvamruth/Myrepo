import tkinter as tk
from tkinter import messagebox

class TicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tech Support Ticket System")

        self.create_widgets()

    def create_widgets(self):
        self.problem_label = tk.Label(self.root, text="Select Problem:")
        self.problem_label.pack()

        self.problem_options = ["Laptop Issue", "Desktop Issue"]
        self.problem_var = tk.StringVar()
        self.problem_var.set(self.problem_options[0])

        self.problem_menu = tk.OptionMenu(self.root, self.problem_var, *self.problem_options)
        self.problem_menu.pack()

        self.description_label = tk.Label(self.root, text="Problem Description:")
        self.description_label.pack()

        self.description_text = tk.Text(self.root, height=5, width=30)
        self.description_text.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_ticket)
        self.submit_button.pack()

    def submit_ticket(self):
        problem = self.problem_var.get()
        description = self.description_text.get("1.0", tk.END).strip()

        if not description:
            messagebox.showerror("Error", "Please provide a problem description.")
        else:
            messagebox.showinfo("Ticket Submitted", f"Ticket for {problem} issue submitted.\nDescription: {description}")
            self.clear_form()

    def clear_form(self):
        self.problem_var.set(self.problem_options[0])
        self.description_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
