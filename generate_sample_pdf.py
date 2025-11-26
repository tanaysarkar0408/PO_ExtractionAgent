from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "PURCHASE ORDER")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "PO Number: PO-2023-001")
    c.drawString(50, height - 120, "Date: 2023-10-27")
    c.drawString(50, height - 140, "Customer: Acme Corp")

    c.drawString(50, height - 180, "Items:")
    
    y = height - 200
    c.drawString(50, y, "1. Item Code: WIDGET-A")
    c.drawString(250, y, "Qty: 100")
    
    y -= 20
    c.drawString(50, y, "2. Item Code: GADGET-B")
    c.drawString(250, y, "Qty: 50")

    c.save()
    print(f"Created {filename}")

if __name__ == "__main__":
    create_sample_pdf("sample_po.pdf")
