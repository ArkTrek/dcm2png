from PIL import Image
import os

def split_image(image_path, output_folder, grid_size=(9, 9)):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Calculate the size of each piece
    grid_width = img_width // grid_size[0]
    grid_height = img_height // grid_size[1]

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split the image into grid_size rows and columns
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            # Calculate the box for each piece
            left = col * grid_width
            upper = row * grid_height
            right = (col + 1) * grid_width
            lower = (row + 1) * grid_height

            # Crop the image
            cropped_img = img.crop((left, upper, right, lower))

            # Save each piece with a unique name
            cropped_img.save(os.path.join(output_folder, f"{os.path.basename(image_path).split('.')[0]}_piece_{row}_{col}.png"))

    print(f"Image '{image_path}' successfully split into {grid_size[0]}x{grid_size[1]} pieces!")

def split_images_in_folder(input_folder, output_folder, grid_size=(9, 9)):
    # Get all image files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add more formats if needed
            image_path = os.path.join(input_folder, filename)
            split_image(image_path, output_folder, grid_size)

if __name__ == "__main__":
    # Path to the input folder containing images
    input_folder = "Epilepsy/dataset"  # Replace with the path to your input folder
    
    # Path to the output folder for split images
    output_folder = "Epilepsy/dataset/split_images"  # Replace with your desired output folder

    # Split images in the specified folder into 9x9 pieces
    split_images_in_folder(input_folder, output_folder)
