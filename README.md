# Font Analyzer for DOCX Files

## Overview

This Python script allows you to analyze fonts used in DOCX (Microsoft Word) documents. It utilizes the `tkinter` library to create a simple file dialog for selecting a DOCX file and then provides a breakdown of the fonts used within the document.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x (You can download it from [python.org](https://www.python.org/downloads/))

## Dependencies

This script relies on the following Python libraries, which can be installed using `pip`:

- `tkinter`: Included with Python, no need for separate installation.
- `python-docx`: Install it using `pip install python-docx`.

## How to Use

1. Clone this repository or download the script `font_analyzer.py` to your local machine.

2. Open your terminal or command prompt.

3. Navigate to the directory where `font_analyzer.py` is located.

4. Run the script .

5. The script will open a file dialog window. Select the DOCX file you want to analyze and click the "Open" button.

6. If the selected file is a DOCX file, the script will analyze the fonts used in the document and display the results in the terminal.

## Example Output

Here's an example of what the script's output might look like:

Selected file: document.docx
Fonts used in the document:
Calibri: 50 occurrences
Times New Roman: 20 occurrences
Arial: 10 occurrences

## Limitations

- This script currently supports only DOCX files. Other document formats are not supported.

## Troubleshooting

If you encounter any issues or errors while using the script, please ensure that you have the required dependencies installed. Additionally, make sure you have selected a valid DOCX file for analysis.

## Contributions

Contributions are welcome! If you have any suggestions or improvements for this script, feel free to create a pull request or open an issue on the GitHub repository.

## License

This script is released under the [MIT License](LICENSE).
