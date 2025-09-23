import fitz 
from PIL import Image
import pytesseract

def pdf_to_text_ocr(pdf_path, output_txt_path):
    pdf_document = fitz.open(pdf_path)
    
    
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        
        for page_num in range(pdf_document.page_count):
            
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            page_text = pytesseract.image_to_string(img)
            output_file.write(f"\n--- Page {page_num + 1} ---\n")
            output_file.write(page_text)
            output_file.write("\n" + "-" * 40 + "\n")
    pdf_document.close()
    print(f"PDF converted to text and saved at '{output_txt_path}'.")


pdf_path = "/Users/modify it for yourselves/downloads/compressed.pdf"
output_txt_path = "/Users/modify it for yourselves/downloads/output.txt"

pdf_to_text_ocr(pdf_path, output_txt_path)
