import tkinter as tk
from tkinter import filedialog
from docx import Document
from collections import Counter

def find_fonts_used(docx_path):
    try:
        doc = Document(docx_path)
        fonts_used = Counter()

        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                font_name = run.font.name
                fonts_used[font_name] += 1

        return fonts_used

    except Exception as e:
        return None

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename(
        title="Select a DOCX File",
        filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
    )

    if file_path:
        print("Selected file:", file_path)

        if file_path.lower().endswith('.docx'):
            fonts_used = find_fonts_used(file_path)
            if fonts_used:
                print("Fonts used in the document:")
                for font, count in fonts_used.items():
                    print(f"{font}: {count} occurrences")
            else:
                print("Failed to extract font information from the document.")
        else:
            print("This program currently supports only DOCX files.")

if __name__ == "__main__":
    open_file_dialog()
