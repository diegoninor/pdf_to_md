# pdf_to_md

A small Python script that converts PDF files to Markdown using [pymupdf4llm](https://pypi.org/project/pymupdf4llm/). It keeps the document's structure (headings, bold text, tables and lists), so the output works well for notes, documentation or as input to LLMs.

## Requirements

- Python 3.8+
- [pymupdf4llm](https://pypi.org/project/pymupdf4llm/)

```bash
pip install -r requirements.txt
```

## Usage

1. Put your PDF files in the `PDF to convert/` folder.
2. Run the script:

```bash
# Convert every PDF in "PDF to convert"
python convertPDF.py

# Convert only specific PDFs
python convertPDF.py path/to/file1.pdf path/to/file2.pdf
```

On Windows you can use `py` instead of `python`

3. The Markdown files are saved in `PDFs converted/`. Each one has the same name as its PDF, for example `report.pdf` → `report.md`.

The script creates both folders if they don't exist yet.

Notes:

- Files in the input and output folders are ignored by git (see `.gitignore`), so personal documents don't end up in the repository.
- Scanned PDFs (images without a text layer) need OCR first. pymupdf4llm only extracts text that is already embedded in the PDF.
