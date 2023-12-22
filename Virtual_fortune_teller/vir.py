import tkinter as tk
from tkinter import messagebox
import random

class VirtualFortuneTellerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Virtual Fortune Teller")

        self.label = tk.Label(master, text="Ask me a question:")
        self.label.pack()

        self.question_entry = tk.Entry(master)
        self.question_entry.pack()

        self.ask_button = tk.Button(master, text="Ask", command=self.get_fortune)
        self.ask_button.pack()

    def get_fortune(self):
        responses = {
            'positive': ['Yes, definitely!', 'You can count on it!', 'Absolutely!', 'For sure!'],
            'neutral': ['Maybe...', "I'm not sure.", 'Ask again later.', "Can't predict now."],
            'negative': ['No way!', 'Not likely.', 'Don\'t count on it.', 'Very doubtful.'],
            'coding_related': ['Your code will compile perfectly!', 'Expect a bug-free day!', 'The algorithm is in your favor.']
        }

        question = self.question_entry.get()
        if not question:
            messagebox.showinfo("Error", "Please enter a question.")
            return

        response_category = random.choice(list(responses.keys()))
        selected_response = random.choice(responses[response_category])

        result_message = f"The Virtual Fortune Teller says: {selected_response}"

        messagebox.showinfo("Fortune Teller Result", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x150")
    root.configure(bg='#FFD700')

    app = VirtualFortuneTellerGUI(root)
    root.mainloop()
