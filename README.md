# Let's Learn Some AWS

This project is focused on learning and experimenting with AWS services. It includes various examples and exercises to understand AWS concepts and tools.

## Features
- Extracts text from PDF files and converts it into Markdown format.
- Extracts images from PDF files, filtering based on dimensions and content.
- Handles PDFs with questions and answers, formatting them appropriately.

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
   pip install -r requirements.txt
   ```

## Usage
1. Place the input PDF file in the `pdf/` directory.
2. Update the `input_pdf`, `output_dir`, and `images_dir` variables in `pdf_to_md_converter.py` as needed.
3. Run the script:
   ```bash
   python pdf_to_md_converter.py
   ```
4. The extracted Markdown files and images will be saved in the specified output directories.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.