from PyPDF2 import PdfMerger
import os

def merge_pdfs(folder_path, output_name):
    merger = PdfMerger()
    
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_files.sort()
    
    for pdf in pdf_files:
        merger.append(os.path.join(folder_path, pdf))
        print(f"Added {pdf}")
    
    merger.write(output_name)
    merger.close()
    print(f"Merged {len(pdf_files)} PDFs into {output_name}")

# Usage
merge_pdfs("./pdfs", "merged_output.pdf")
