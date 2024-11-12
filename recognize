import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def pdf_to_text_ocr(pdf_path, output_txt_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Create or open the output text file
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        # Iterate over each page
        for page_num in range(pdf_document.page_count):
            # Get the page and render as an image
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            
            # Convert image to PIL format
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Perform OCR on the image
            page_text = pytesseract.image_to_string(img)
            
            # Write the page number and the text to the file
            output_file.write(f"\n--- Page {page_num + 1} ---\n")
            output_file.write(page_text)
            output_file.write("\n" + "-" * 40 + "\n")

    # Close the PDF document
    pdf_document.close()
    print(f"PDF converted to text and saved as '{output_txt_path}'.")

# Specify the path to your PDF file and desired output text file
pdf_path = "/Users/admin/downloads/k3c1-compressed.pdf"
output_txt_path = "/Users/admin/downloads/k3c1_ocr_output.txt"

# Run the function
pdf_to_text_ocr(pdf_path, output_txt_path)
