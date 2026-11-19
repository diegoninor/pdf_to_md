"""Converts PDF files to Markdown and saves them in the "PDFs converted" folder.

Usage:
    py convertPDF.py                     -> converts all PDFs in "PDF to convert"
    py convertPDF.py file1.pdf ...       -> converts only the given PDFs
"""

import sys
from pathlib import Path

import pymupdf4llm

# Script folder, input subfolder and output subfolder
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "PDF to convert"
OUTPUT_DIR = BASE_DIR / "PDFs converted"


def convert_pdf(pdf_path: Path) -> Path:
    """Converts a PDF to Markdown and returns the path of the generated .md file."""
    # Extract Markdown (headings, bold text, tables, lists...)
    markdown_text = pymupdf4llm.to_markdown(str(pdf_path))

    # Save in the output subfolder with the same name as the PDF
    md_path = OUTPUT_DIR / f"{pdf_path.stem}.md"
    md_path.write_text(markdown_text, encoding="utf-8")
    return md_path


def main() -> None:
    # Create the input and output folders if they don't exist
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    # PDFs passed as arguments, or all of those in the "PDF to convert" folder
    if len(sys.argv) > 1:
        pdfs = [Path(p) for p in sys.argv[1:]]
    else:
        pdfs = sorted(INPUT_DIR.glob("*.pdf"))

    if not pdfs:
        print(f"No PDF files found in: {INPUT_DIR}")
        return

    for pdf in pdfs:
        try:
            destination = convert_pdf(pdf)
            print(f"✔ {pdf.name} → {destination}")
        except Exception as e:
            print(f"✘ Error converting {pdf.name}: {e}")


if __name__ == "__main__":
    main()
