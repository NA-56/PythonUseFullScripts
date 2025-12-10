import os
from pathlib import Path
from PyPDF2 import PdfMerger, PdfWriter, PdfReader

def merge_pdfs(folder_path, output_filename="merged.pdf", add_toc=True):
    """
    Merges all PDF files in a folder into a single PDF file with bookmarks.
    
    Args:
        folder_path: Path to the folder containing PDF files
        output_filename: Name of the output merged PDF file
        add_toc: Whether to add bookmarks and TOC page
    """
    try:
        # Get all PDF files in the folder
        pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])
        
        if not pdf_files:
            print(f"No PDF files found in {folder_path}")
            return
        
        print(f"Found {len(pdf_files)} PDF file(s)")
        
        # Create PDF merger object
        merger = PdfMerger()
        page_offset = 0
        toc_entries = []
        
        # Add each PDF file to the merger and create a bookmark at its start
        for pdf_file in pdf_files:
            file_path = os.path.join(folder_path, pdf_file)
            print(f"Adding: {pdf_file}")
            
            # Get the number of pages
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
            
            # Store TOC entry (filename without extension, starting page)
            clean_name = os.path.splitext(pdf_file)[0].replace('_', ' ')
            toc_entries.append((clean_name, page_offset))
            

            # Append and add bookmark pointing to the start of this appended file
            merger.append(file_path, outline_item=clean_name)
            page_offset += num_pages
        
        # Write the merged PDF (bookmarks already added)
        output_path = os.path.join(folder_path, output_filename)
        merger.write(output_path)
        merger.close()
        
        print(f"\n✓ Successfully merged {len(pdf_files)} PDFs")
        print(f"✓ Output saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

# ...existing code...
if __name__ == "__main__":
    # Specify the folder path containing PDFs
    folder = r"folder path"
    
    # Run the merge with bookmarks
    merge_pdfs(folder, "Merged_files.pdf", add_toc=True)
