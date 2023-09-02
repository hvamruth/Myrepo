import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class TicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tech Support Ticket System")

        self.create_widgets()

    def create_widgets(self):
        self.problem_label = tk.Label(self.root, text="Select Problem:")
        self.problem_label.grid(row=0, column=0, sticky=tk.W)

        self.problem_options = ["Laptop Issue", "Desktop Issue"]
        self.problem_var = tk.StringVar()
        self.problem_var.set(self.problem_options[0])

        self.problem_menu = tk.OptionMenu(self.root, self.problem_var, *self.problem_options)
        self.problem_menu.grid(row=0, column=1, sticky=tk.W)

        self.model_label = tk.Label(self.root, text="Model Number:")
        self.model_label.grid(row=1, column=0, sticky=tk.W)

        self.model_entry = tk.Entry(self.root)
        self.model_entry.grid(row=1, column=1, sticky=tk.W)

        self.name_label = tk.Label(self.root, text="Computer/Laptop Name:")
        self.name_label.grid(row=2, column=0, sticky=tk.W)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=2, column=1, sticky=tk.W)

        self.error_label = tk.Label(self.root, text="Error Code:")
        self.error_label.grid(row=3, column=0, sticky=tk.W)

        self.error_entry = tk.Entry(self.root)
        self.error_entry.grid(row=3, column=1, sticky=tk.W)

        self.description_label = tk.Label(self.root, text="Problem Description:")
        self.description_label.grid(row=4, column=0, sticky=tk.W)

        self.description_text = tk.Text(self.root, height=5, width=30)
        self.description_text.grid(row=4, column=1, sticky=tk.W)

        self.email_label = tk.Label(self.root, text="Your Email:")
        self.email_label.grid(row=5, column=0, sticky=tk.W)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=5, column=1, sticky=tk.W)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_ticket)
        self.submit_button.grid(row=6, columnspan=2, pady=10)

    def submit_ticket(self):
        problem = self.problem_var.get()
        model = self.model_entry.get()
        name = self.name_entry.get()
        error_code = self.error_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()
        user_email = self.email_entry.get()

        if not description or not user_email:
            messagebox.showerror("Error", "Please provide a problem description and your email.")
        else:
            self.save_ticket(problem, model, name, error_code, description, user_email)
            self.send_ticket_email(problem, model, name, error_code, description, user_email)
            messagebox.showinfo("Ticket Submitted", "Ticket submitted successfully.")
            self.clear_form()

    def save_ticket(self, problem, model, name, error_code, description, user_email):
        with open("tickets.txt", "a") as file:
            file.write(f"Problem: {problem}\nModel: {model}\nComputer/Laptop Name: {name}\nError Code: {error_code}\nDescription: {description}\nUser Email: {user_email}\n\n")

    def send_ticket_email(self, problem, model, name, error_code, description, user_email):
        from_email = "your_email@example.com"  # Replace with your email
        to_email = "itsupport@waterinnovation.co.in"  # Replace with support's email
        subject = f"New Tech Support Ticket: {problem}"

        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        body = f"Problem: {problem}\nModel: {model}\nComputer/Laptop Name: {name}\nError Code: {error_code}\nDescription: {description}\nUser Email: {user_email}"
        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("mail.waterinnovation.co.in", 465)  # Using SMTP server and port for waterinnovation.co.in domain
            server.starttls()
            server.login(from_email, "your_password")  # Replace with your email password
            server.sendmail(from_email, to_email, message.as_string())
            server.quit()
        except Exception as e:
            print("Error sending email:", e)

    def clear_form(self):
        self.problem_var.set(self.problem_options[0])
        self.model_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.error_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)
        self.email_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
