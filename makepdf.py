
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import os

def create_pdf():
    c = canvas.Canvas("content_pdf2.pdf", pagesize=letter)
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, 700, "Creating PDFs with Python")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 14)
    c.drawString(50, 660, "In this tutorial, we will demonstrate how to create PDF files using Python.")
    c.drawString(50, 640, "Python is a versatile programming language that can be used to create different types of files, including PDFs.")
    c.drawString(50, 620, "By the end of this tutorial, you will be able to generate PDF files using Python and the ReportLab library.")

    image_path = os.path.join(os.getcwd(), "incoming/lion-style-1-display.jpg")

    c.drawImage(image_path, 200, 200, width=400, height=500)

    c.save()

if __name__ == "__main__":
    create_pdf()




# Usage
# create_pdf_with_image_and_text("incoming/lion-style-1-display.jpg", "Sample Text", "output.pdf", "https://www.example.com")
