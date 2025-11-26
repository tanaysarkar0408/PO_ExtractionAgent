from po_agent.tools.pdf_tools import read_pdf_content
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inspect_pdf.py <pdf_path>")
        sys.exit(1)
    
    text = read_pdf_content(sys.argv[1])
    print("--- RAW PDF TEXT ---")
    print(text)
    print("--------------------")
