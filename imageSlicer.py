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

            # Save each piece
            cropped_img.save(os.path.join(output_folder, f"piece_{row}_{col}.png"))

    print(f"Image successfully split into {grid_size[0]}x{grid_size[1]} pieces!")

if __name__ == "__main__":
    # Path to the input image
    image_path = "Epilepsy//dataset//04-0001-000001.png"  # Replace with the path to your image
    
    # Path to the output folder
    output_folder = "Epilepsy//dataset"  # Replace with your desired output folder

    # Split the image into 9x9 pieces
    split_image(image_path, output_folder)
