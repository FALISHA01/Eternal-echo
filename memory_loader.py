from PyPDF2 import PdfReader
import os

def load_text_file(path):
    """Load plain text from a .txt file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_pdf(path):
    """Extract readable text from all pages of a PDF file."""
    reader = PdfReader(path)
    return "\n".join([page.extract_text() or '' for page in reader.pages])

def load_memories_from_folder(folder_path):
    """Go through all files in the folder and return full combined text."""
    all_text = ""
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith(".txt"):
            all_text += load_text_file(full_path) + "\n"
        elif file.endswith(".pdf"):
            all_text += load_pdf(full_path) + "\n"
        # Add more types later (e.g., .json for Twitter exports)
    return all_text
