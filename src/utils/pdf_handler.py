from PyPDF2 import PdfReader

def get_pdf_text(docs):
    """Extracts text from a list of PDF files.

    Args:
        docs: A list of PDF file objects.

    Returns:
        A string containing the extracted text from all PDF files.
    """
    text = ""
    for pdf in docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text