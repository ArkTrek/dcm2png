import os
import pydicom
from PIL import Image
import numpy as np

def convert_dcm_to_png(input_folder, output_folder):
    # Walk through the input folder and its subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".dcm"):
                dcm_file_path = os.path.join(root, file)

                # Read the DICOM file
                dicom = pydicom.dcmread(dcm_file_path)

                # Convert DICOM pixel data to a numpy array
                image_data = dicom.pixel_array

                # Normalize the image data to 8-bit (0-255) range
                image_data = ((image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data))) * 255
                image_data = image_data.astype(np.uint8)

                # Convert numpy array to PIL Image object
                img = Image.fromarray(image_data)

                # Generate a PNG file name using the DICOM file name
                png_file_name = file.replace('.dcm', '.png')

                # Save the image to the output folder
                output_file_path = os.path.join(output_folder, png_file_name)
                img.save(output_file_path)

                print(f"Converted {dcm_file_path} to {output_file_path}")

if __name__ == "__main__":
    input_folder = "Epilepsy\\Controls"  # Replace with your input folder path
    output_folder = "Epilepsy\\dataset"     # Replace with your output folder path
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert all DICOM files to PNG
    convert_dcm_to_png(input_folder, output_folder)
