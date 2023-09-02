import tkinter as tk
from tkinter import filedialog
from docx import Document

def find_fonts_used(docx_path):
    try:
        doc = Document(docx_path)
        fonts_used = set()

        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                font_name = run.font.name
                fonts_used.add(font_name)

        return fonts_used

    except Exception as e:
        return str(e)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename(
        title="Select a Document or Text File",
        filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("All Files", "*.*")]
    )

    if file_path:
        print("Selected file:", file_path)

        if file_path.lower().endswith('.docx'):
            fonts_used = find_fonts_used(file_path)
            if fonts_used:
                print("Fonts used in the document:")
                for font in fonts_used:
                    print(font)
            else:
                print("Failed to extract font information from the document.")
        else:
            print("This program currently supports only DOCX files.")

if __name__ == "__main__":
    open_file_dialog()
