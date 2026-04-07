from pypdf import PdfReader
import io

def PDFReader(source, from_bytes=False):
    if from_bytes:
        reader = PdfReader(io.BytesIO(source))
    else:
        reader = PdfReader(source)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text