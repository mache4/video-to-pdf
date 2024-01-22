from PIL import Image
import os

def split_and_save(input_folder, output_folder, split_width):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)

            # Get the width and height of the image
            width, height = img.size

            # Specify the split width (vertical split position)
            if 0 < split_width < width:
                # Crop the left part (first book page)
                left_img = img.crop((0, 0, split_width, height))
                left_path = os.path.join(output_folder, f"{file_name.split('.')[0]}_left.jpg")
                left_img.save(left_path)

                # Crop the right part (second book page)
                right_img = img.crop((split_width, 0, width, height))
                right_path = os.path.join(output_folder, f"{file_name.split('.')[0]}_right.jpg")
                right_img.save(right_path)

if __name__ == "__main__":
    input_folder = "gradually_shifted_cropped_pages"
    output_folder = "split_pages"
    os.makedirs(output_folder, exist_ok=True)

    # Specify the width at which to perform the vertical split
    split_width = 416

    split_and_save(input_folder, output_folder, split_width)
