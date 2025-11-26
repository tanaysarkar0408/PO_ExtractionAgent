import pypdf
from typing import Optional

def read_pdf_content(file_path: str) -> Optional[str]:
    """
    Reads text content from a PDF file.
    
    Args:
        file_path: Absolute path to the PDF file.
        
    Returns:
        Extracted text as a string, or None if reading fails.
    """
    try:
        text = ""
        with open(file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return None
