import os
import re
from PyPDF2 import PdfReader
import fitz  # PyMuPDF
try:
    from PIL import Image
    import io
except ImportError:
    Image = None
    io = None


def ensure_directories_exist(*directories):
    """Ensure the specified directories exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def extract_questions_from_text(page_text):
    """
    - Extracts all questions from a PDF page as a list of Markdown strings.
    - Improves formatting:
        - Adds an empty line after "Question" and after lines ending with '.' or '?'.
        - Keeps option lines (e.g., "A.", "B.") in a single line.
        - Joins non-option text into paragraphs.
    - Removes ' Most Voted' from option lines only, even if it appears in the middle of a line or after a line break.
    - Places 'Correct Answer:' lines as a separate line.
    """
    questions = []
    current = []
    in_question = False
    previous_line = ""
    option_pattern = re.compile(r"^([A-G]\.)")
    paragraph = []
    for line in page_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Question #"):
            if current:
                # Flush any pending paragraph
                if paragraph:
                    current.append(" ".join(paragraph))
                    paragraph = []
                questions.append("\n".join(current))
                current = []
            in_question = True
            current.append(f"## {line}\n")  # Add empty line after Question
            previous_line = ""
        elif in_question:
            if option_pattern.match(line):
                # Flush any pending paragraph
                if paragraph:
                    current.append(" ".join(paragraph))
                    paragraph = []
                previous_line = f"- {line}"
                current.append(previous_line)
            elif previous_line and (current and current[-1].startswith("- ")):
                # Append to previous option line (keep in one line)
                appended = line
                # If 'Correct Answer:' is in the appended text, split it out
                if 'Correct Answer:' in appended:
                    before, after = appended.split('Correct Answer:', 1)
                    current[-1] = f"{current[-1]} {before.strip()}"
                    current.append(f"\nCorrect Answer: {after.strip()}")
                    previous_line = ""
                else:
                    current[-1] = f"{current[-1]} {appended}"
                    previous_line = current[-1]
            else:
                # Accumulate non-option lines into a paragraph
                paragraph.append(line)
                # If line ends with . or ?, flush paragraph and add empty line
                if line.endswith('.') or line.endswith('?'):
                    current.append(" ".join(paragraph))
                    current.append("")
                    paragraph = []
                previous_line = ""
    # Flush any remaining paragraph and question
    if paragraph:
        current.append(" ".join(paragraph))
    if current:
        questions.append("\n".join(current))
    # Remove ' Most Voted' from any option lines in the final output (extra safety)
    cleaned_questions = []
    for q in questions:
        cleaned_lines = []
        for l in q.split('\n'):
            if l.strip().startswith('- '):
                cleaned_lines.append(l.replace(' Most Voted', ''))
            else:
                cleaned_lines.append(l)
        cleaned_questions.append('\n'.join(cleaned_lines))
    return cleaned_questions


def save_markdown(output_pages_dir, question_number, formatted_text):
    """Save the formatted text as a Markdown file for each question."""
    output_file = os.path.join(output_pages_dir, f"page_{question_number}.md")
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(formatted_text)


def extract_images(pdf_document, question_number, output_images_dir, page_index, contains_hotspot):
    """Extract images from a PDF page and save them using the question number, with hotspot and size filtering."""
    pdf_page = pdf_document[page_index]
    images = pdf_page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        width, height = base_image["width"], base_image["height"]

        # Skip irrelevant images (size is less than 300x300)
        if not contains_hotspot or width < 300 or height < 300 or (width == 345 and height == 350):
            continue

        # Save the image with question number
        print(f"Extracting image {img_index + 1} for question {question_number} with dimensions {width}x{height}")
        image_file = os.path.join(output_images_dir, f"page_{question_number}_image_{img_index + 1}.{image_ext}")
        with open(image_file, "wb") as img_file:
            img_file.write(image_bytes)


def process_pdf(input_pdf, output_pages_dir, output_images_dir):
    """Process the PDF to extract questions and images."""
    # Ensure the input PDF file exists
    if not os.path.exists(input_pdf):
        raise FileNotFoundError(f"The input PDF file '{input_pdf}' was not found. Please check the file path.")

    # Ensure the output directories exist
    ensure_directories_exist(output_pages_dir, output_images_dir)

    # Read the PDF file
    reader = PdfReader(input_pdf)
    pdf_document = fitz.open(input_pdf)

    # Loop through each page
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if i == 0:
            print(page_text)  # Print the first page text for debugging

        # Extract all questions from the page
        questions = extract_questions_from_text(page_text)
        for q in questions:
            m = re.search(r"Question #(\d+)", q)
            if m:
                qnum = m.group(1)
                save_markdown(output_pages_dir, qnum, q)
                contains_hotspot = "HOTSPOT" in page_text.upper()
                extract_images(pdf_document, qnum, output_images_dir, i, contains_hotspot)
    print(f"PDF has been successfully converted into Markdown files and images in {output_pages_dir} and {output_images_dir}")


if __name__ == "__main__":
    # Define the input PDF file and output directories
    exam_dir = "MLA-C01"
    input_pdf = f"{exam_dir}/pdf/202506/with_answers.pdf" # only pdf with answers needed here
    output_pages_dir = f"{exam_dir}/pages"
    output_images_dir = f"{exam_dir}/images"

    # Process the PDF
    process_pdf(input_pdf, output_pages_dir, output_images_dir)