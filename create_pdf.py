from reportlab.pdfgen import canvas
from PIL import Image
import os

def create_pdf(input_folder, output_pdf):
    c = canvas.Canvas(output_pdf)

    # Get a sorted list of file names
    file_names = sorted(os.listdir(input_folder), key=lambda x: int(x.split("_")[1].split(".")[0]))

    for file_name in file_names:
        if file_name.endswith("_left.jpg") or file_name.endswith("_right.jpg"):
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)

            # Add the image to the PDF
            c.drawImage(image_path, 0, 0, width=600, height=800)
            c.showPage()

    c.save()

if __name__ == "__main__":
    input_folder = "split_pages"
    output_pdf = "output.pdf"

    create_pdf(input_folder, output_pdf)
