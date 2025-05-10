import os
from PyPDF2 import PdfReader
import fitz  # PyMuPDF


def ensure_directories_exist(*directories):
    """Ensure the specified directories exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def extract_text_as_markdown(page_text):
    """Extract and format text from a PDF page as Markdown."""
    formatted_text = []
    question_found = False
    previous_line = ""

    for line in page_text.splitlines():
        line = line.strip()
        if not line:  # Ignore empty lines
            continue

        if not question_found:
            if line.startswith("Question"):
                question_found = True
            else:
                continue

        if line.startswith("Question #"):
            formatted_text.append(f"## {line}\n\n")  # Bold for questions
        elif line.startswith(("A.", "B.", "C.", "D.", "E.", "F.", "G.")):
            previous_line = f"- {line}"
            formatted_text.append(previous_line)
        elif previous_line:
            formatted_text[-1] = f"{formatted_text[-1]} {line}"
            previous_line = ""
        else:
            if formatted_text and not formatted_text[-1].endswith("."):
                formatted_text[-1] = f"{formatted_text[-1]} {line}"
            else:
                formatted_text.append(line)

    return "\n\n".join(formatted_text)


def save_markdown(output_dir, page_number, formatted_text):
    """Save the formatted text as a Markdown file."""
    output_file = os.path.join(output_dir, f"page_{page_number}.md")
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(formatted_text)


def extract_images(pdf_document, page_index, images_dir, contains_hotspot):
    """Extract images from a PDF page."""
    pdf_page = pdf_document[page_index]
    for img_index, img in enumerate(pdf_page.get_images(full=True)):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        width, height = base_image["width"], base_image["height"]

        # Skip irrelevant images
        if not contains_hotspot or width < 200 or height < 200:
            continue

        # Save the image
        print(f"Extracting image {img_index + 1} from page {page_index + 1} with dimensions {width}x{height}")
        image_file = os.path.join(images_dir, f"page_{page_index + 1}_image_{img_index + 1}.{image_ext}")
        with open(image_file, "wb") as img_file:
            img_file.write(image_bytes)


def process_pdf(input_pdf, output_dir, images_dir):
    """Process the PDF to extract text and images."""
    # Ensure the input PDF file exists
    if not os.path.exists(input_pdf):
        raise FileNotFoundError(f"The input PDF file '{input_pdf}' was not found. Please check the file path.")

    # Ensure the output directories exist
    ensure_directories_exist(output_dir, images_dir)

    # Read the PDF file
    reader = PdfReader(input_pdf)
    pdf_document = fitz.open(input_pdf)

    # Loop through each page
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if i == 0:
            print(page_text)  # Print the first page text for debugging

        # Extract and save text as Markdown
        formatted_text = extract_text_as_markdown(page_text)
        save_markdown(output_dir, i + 1, formatted_text)

        # Check if the page contains the text "HOTSPOT"
        contains_hotspot = "HOTSPOT" in page_text.upper()

        # Extract and save images
        extract_images(pdf_document, i, images_dir, contains_hotspot)

    print(f"PDF has been successfully converted into Markdown files and images in {output_dir} and {images_dir}")


if __name__ == "__main__":
    # Define the input PDF file and output directories
    input_pdf = ""
    output_dir = ""
    images_dir = ""

    # Process the PDF
    process_pdf(input_pdf, output_dir, images_dir)