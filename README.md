# Let's Learn Some AWS

This project provides a workflow to extract AWS exam questions from PDFs, convert them to Markdown and then to JSON, and display them in an interactive quiz website.

## Features
- Extracts each question from PDF as a separate Markdown file.
- Converts Markdown questions to structured JSON.
- Extracts and saves images from PDFs, skipping blank/white images and the first image per page.
- Removes "Most Voted" from options.
- Extracts correct answers and formats them for quiz use.
- Interactive quiz web UI (HTML/JS) with:
  - Grid of questions, color-coded by answer status
  - Modal for each question with separated title/content
  - Option selection with immediate feedback
  - Left/right arrow navigation (buttons and keyboard)
  - Proper handling of newlines and formatting

## Prerequisites
- Python installed
- Required Python libraries: `PyPDF2`, `PyMuPDF`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd lets-learn-some-aws
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r AIF-C01/requirements.txt
   ```

## Usage
1. Place the input PDF file in the `AIF-C01/pdf/` directory.
2. Update the `input_pdf`, `output_dir`, and `images_dir` variables in `AIF-C01/pdf_to_md_converter.py` as needed.
3. Run the PDF-to-Markdown script:
   ```bash
   python AIF-C01/pdf_to_md_converter.py
   ```
4. Run the Markdown-to-JSON script:
   ```bash
   python AIF-C01/md_to_json.py
   ```
5. Open `index.html` in your browser to use the interactive quiz UI.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.