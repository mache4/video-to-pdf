from PIL import Image
import os

def crop_and_save(input_folder, output_folder, crop_box, initial_horizontal_shift, shift_increment):
    accumulated_shift = initial_horizontal_shift

    # Get a sorted list of file names
    file_names = sorted(os.listdir(input_folder), key=lambda x: int(x.split("_")[1].split(".")[0]))

    for i, file_name in enumerate(file_names):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)

            # Add the accumulated horizontal shift to the cropping box
            adjusted_box = (
                crop_box[0] + accumulated_shift,
                crop_box[1],
                crop_box[2] + accumulated_shift,
                crop_box[3]
            )

            # Crop the image based on the adjusted coordinates
            cropped_img = img.crop(adjusted_box)

            # Save the cropped image to the output folder
            output_path = os.path.join(output_folder, file_name)
            cropped_img.save(output_path)

            # Update the accumulated shift for the next image
            accumulated_shift += shift_increment

    print("Cropping and shifting completed.")

if __name__ == "__main__":
    input_folder = "frames"
    output_folder = "gradually_shifted_cropped_pages"
    os.makedirs(output_folder, exist_ok=True)

    # Specify the coordinates (left, top, right, bottom) for cropping
    crop_box = (180, 64, 1008, 691)

    # Specify the initial horizontal shift and the increment for each image
    initial_horizontal_shift = 0
    shift_increment = 0.27

    crop_and_save(input_folder, output_folder, crop_box, initial_horizontal_shift, shift_increment)