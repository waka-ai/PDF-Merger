
# 📄 PDF Merger Tool

A lightweight Python utility that merges multiple PDF files from a specified folder into a single combined PDF document.

This tool is useful for combining reports, assignments, scanned documents, invoices, or any collection of PDFs into one organized file.

---

## 🚀 Features

* Merges all PDF files in a folder
* Automatically sorts files alphabetically before merging
* Simple and minimal code
* Fast and efficient
* Easy to customize

---

## 🛠 Tech Stack

* Python 3.x
* [PyPDF2](https://pypi.org/project/PyPDF2/) library

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pdf-merger-tool.git
cd pdf-merger-tool
```

Install dependencies:

```bash
pip install PyPDF2
```

---

## ▶️ Usage

1. Place all PDFs you want to merge inside a folder (e.g., `pdfs/`).
2. Update the folder path and output file name if needed:

```python
merge_pdfs("./pdfs", "merged_output.pdf")
```

3. Run the script:

```bash
python pdf_merger.py
```

---

## 📁 Example Folder Structure

Before:

```
project/
│
├── pdf_merger.py
└── pdfs/
    ├── 1_intro.pdf
    ├── 2_chapter.pdf
    ├── 3_summary.pdf
```

After running:

```
project/
│
├── merged_output.pdf
├── pdf_merger.py
└── pdfs/
```

---

## ⚙️ How It Works

1. Reads all `.pdf` files from the specified folder.
2. Sorts them alphabetically.
3. Appends them to a `PdfMerger` object.
4. Writes the final merged file to disk.

---

## ⚠️ Important Notes

* Files are merged in **alphabetical order**.
* Ensure PDFs are named correctly if order matters (e.g., `01_`, `02_`, `03_`).
* The script does not handle corrupted or password-protected PDFs.
* Output file will be overwritten if it already exists.

---

## 🔧 Customization Ideas

You can extend this tool by:

* Adding command-line arguments (`argparse`)
* Allowing manual file selection
* Supporting drag-and-drop
* Adding GUI (Tkinter / PyQt)
* Adding password-protected PDF support
* Adding recursive folder scanning
* Preventing overwrite of existing files

---

## 💼 Use Cases

* Combining scanned documents
* Merging monthly reports
* Creating consolidated assignments
* Merging invoices or contracts
* Preparing documentation bundles

---

## 📄 License

MIT License — Free to use and modify.
