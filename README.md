# AWS Certification Practice Tests

This project is an interactive, web-based platform for practicing AWS certification exams. It provides a clean, responsive UI to take practice tests, review answers, and track progress.

## Features

- **Multi-Exam Support**: Easily switch between different AWS certification practice tests from the main landing page.
- **Interactive Quiz UI**:
    - A grid-based navigation system shows all questions, color-coded by their answer status (correct, incorrect, unanswered).
    - Questions are displayed in a clean, readable modal with easy navigation.
    - Supports multiple question types, including single-choice, multiple-choice, and hotspot dropdowns.
- **Client-Side Progress Tracking**: Your progress, including answered questions, marked questions, and selected answers, is saved in your browser's local storage.
- **Responsive Design**: The interface is fully responsive and works seamlessly on both desktop and mobile devices.

## Available Practice Tests

- **AIF-C01**: AWS Certified AI Practitioner
- **MLA-C01**: AWS Certified Machine Learning Engineer - Associate

## Usage

No installation is needed to use the practice tests. Simply open the `index.html` file in your web browser.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/lets-learn-some-aws.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd lets-learn-some-aws
    ```
3.  **Open `index.html` in your browser.**

## For Developers: Adding New Exams

The questions for each exam are stored in a structured JSON file. To add a new exam, you'll need to follow the data processing pipeline to generate this JSON file from a source PDF.

### Prerequisites

- Python 3.x
- Required Python libraries are listed in `requirements.txt`. Install them using:
  ```bash
  pip install -r requirements.txt
  ```

### Data Processing Pipeline

1.  **PDF to Markdown (`pdf_to_md_converter.py`)**:
    - This script converts a PDF of practice questions into individual Markdown files for each question.
    - Place your source PDF in the `pdf/` directory within a new exam folder (e.g., `NEW-EXAM/pdf/`).
    - The script extracts text and images, saving them into `pages/` and `images/` directories respectively.

2.  **Markdown to JSON (`md_to_json.py`)**:
    - This script processes the Markdown files, parses the question, options, and answer, and compiles them into a single `questions.json` file.
    - This JSON file is then loaded by the corresponding HTML page for the exam.

### Project Structure

The project is organized by exam code to keep the content for each test self-contained.

```
/
├── AIF-C01/
│   ├── images/         # Images extracted from the PDF
│   ├── pages/          # Markdown files for each question
│   ├── pdf/            # Source PDF file (optional)
│   └── questions.json  # Final JSON data for the quiz
├── MLA-C01/
│   └── ... (same structure as AIF-C01)
├── index.html          # Main landing page to select an exam
├── aif-c01.html        # Quiz page for the AIF-C01 exam
├── mla-c01.html        # Quiz page for the MLA-C01 exam
├── pdf_to_md_converter.py # Script to convert PDF to Markdown
├── md_to_json.py       # Script to convert Markdown to JSON
└── README.md
```

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions for adding new exams or enhancing the UI are welcome.

## License

This project is licensed under the MIT License.