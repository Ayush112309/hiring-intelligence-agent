# tools/pdf_parser.py

import fitz 


def load_pdf_text(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    """

    text = ""

    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                page_text = page.get_text()
                if page_text:
                    text += page_text + "\n"

        return text.strip()

    except Exception as e:
        print(f"❌ Error reading PDF {file_path}: {e}")
        return ""