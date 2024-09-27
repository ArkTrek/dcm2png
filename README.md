# DICOM to PNG Converter

This repository contains a Python script that converts DICOM (.dcm) files into PNG format. The script traverses through a folder and its subfolders, identifies all `.dcm` files, and converts them to `.png` files. All the PNG files are saved in a single output folder.

Additionally, this script can split the converted PNG files into 9x9 grid pieces if the DICOM image arrangement necessitates it (such as for large images or when image segmentation is required).

## What are DICOM Files?

**DICOM** (Digital Imaging and Communications in Medicine) is a standard for handling, storing, and transmitting medical images and related information. It is used globally in medical imaging for the interoperability of systems and devices, enabling the integration of imaging devices (such as MRI, CT, X-ray scanners) with hospitals and clinics' IT systems.

### Key Features of DICOM:
- **Medical Image Format**: Used for medical imaging data such as MRI, CT scans, X-rays, ultrasound, and more.
- **Embedded Metadata**: Contains extensive metadata, such as patient information, image acquisition parameters, and hospital or clinic information.
- **Cross-Modality Support**: Supports multiple imaging modalities like radiography, mammography, ultrasound, CT, MRI, and nuclear medicine.
- **Interoperability**: Ensures compatibility across different medical systems and imaging devices, enabling universal interpretation and sharing of images.

### Components of a DICOM File:
1. **Header**: Contains metadata such as patient name, ID, modality (e.g., MRI, CT), and dimensions.
2. **Pixel Data**: The actual image data, which can represent a single 2D image or a series of slices for 3D data.
3. **Tags**: Labels used for metadata fields. Each tag is identified by a unique hexadecimal pair (e.g., `0010,0010` for the patient's name).

## Requirements

- Python 3.x
- `pydicom` library for reading DICOM files.
- `Pillow` library for saving the images as PNG.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/arktrek/dcm2png.git
    cd dcm2png
    ```

2. Install the required Python packages:

    ```bash
    pip install pydicom Pillow
    ```

## Usage

1. Place your DICOM files inside a folder. The script will also process files in any subfolders.

2. Modify the `input_folder` and `output_folder` variables in the script to point to your input folder containing DICOM files and the output folder where the PNG files will be saved.

3. Run the script:

    ```bash
    python dcm2png.py
    ```

4. After the script runs, check the `output_folder` for the converted PNG files.

5. If you need to split the PNG files into 9x9 grid pieces, you can run the **Image Splitter** part of the script. This is helpful for large images or image segmentation.

### Image Splitter Usage

1. The script can automatically split each converted PNG into 9x9 pieces if the DICOM image is large or if segmentation is required.

2. To activate the image splitting functionality, make sure to set `split_images = True` in the script. You can also adjust the grid size by modifying the `grid_size` variable.

3. The output PNG pieces will be saved in a separate folder within the `output_folder` under the `pieces` subdirectory.

```python
    python split_images.py

```
This will split the PNG images into 9x9 pieces and save them to the pieces folder.

## Example

If your folder structure looks like this:
/path/to/dicom/folder
├── file1.dcm
├── file2.dcm
└── subfolder
    └── file3.dcm


After running the script, all PNG files will be saved in the output folder you specify.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to improving this script!

## Contact

If you have any questions, feel free to reach out via GitHub issues.

---

Happy converting! 😊

