import tkinter as tk
from tkinter import ttk
import pyautogui as pg
import time

def automate(typing_text, repetitions, press_enter):
    # Give some time to switch to the desired application
    time.sleep(5)

    # Loop to perform the automation
    for _ in range(repetitions):
        pg.write(typing_text)
        if press_enter:
            pg.press('enter')
        time.sleep(1)  # Add a small delay between repetitions

def start_automation():
    # Get input values from the GUI
    text_to_type = text_entry.get()
    repetitions = int(repetitions_entry.get())
    press_enter = enter_checkbox_var.get()

    # Start the automation
    automate(text_to_type, repetitions, press_enter)

# Create the main window
root = tk.Tk()
root.title("Automation GUI")

# Create and place widgets in the window
label1 = ttk.Label(root, text="Enter Text to Type:")
label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

text_entry = ttk.Entry(root, width=30)
text_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

label2 = ttk.Label(root, text="Number of Repetitions:")
label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

repetitions_entry = ttk.Entry(root, width=10)
repetitions_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

enter_checkbox_var = tk.BooleanVar()
enter_checkbox = ttk.Checkbutton(root, text="Press Enter after each repetition", variable=enter_checkbox_var)
enter_checkbox.grid(row=2, column=0, columnspan=2, pady=10)

start_button = ttk.Button(root, text="Start Automation", command=start_automation)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()

