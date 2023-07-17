import cv2
import os
import re
import pytesseract

def extract_invoice_info(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR (Optical Character Recognition) to extract text
    extracted_text = pytesseract.image_to_string(gray)

    # Extract invoice number using regular expressions
    invoice_number = re.search(r"No:\s*(\w+)", extracted_text)
    if invoice_number:
        invoice_number = invoice_number.group(1)

    # Extract date using regular expressions
    date = re.search(r"Date:\s*(\d{2}.\d{2}.\d{4})", extracted_text)
    if date:
        date = date.group(1)

    # Extract amount using regular expressions
    amount = re.search(r"Total\s*(\$\d{3})", extracted_text)
    if amount:
        amount = amount.group(1)

    # Return the extracted information
    return {
        "invoice_number": invoice_number,
        "date": date,
        "amount": amount
    }

def process_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Create the full file path
            image_path = os.path.join(folder_path, file)

            # Process the image and extract invoice information
            result = extract_invoice_info(image_path)

            # Print the results
            print("Image:", file)
            print("Invoice Number:", result["invoice_number"])
            print("Date:", result["date"])
            print("Amount:", result["amount"])
            print()

# Example usage
folder_path = "/home/lam/CIM"
process_images_in_folder(folder_path)
