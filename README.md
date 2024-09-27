# DICOM to PNG Converter

This repository contains a Python script that converts DICOM (.dcm) files into PNG format. The script traverses through a folder and its subfolders, identifies all `.dcm` files, and converts them to `.png` files. All the PNG files are saved in a single output folder.

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

### Why Convert DICOM to PNG?
- **Visualization**: PNG is a widely used image format supported by almost all software applications, making it easier to visualize medical images outside specialized medical software.
- **Sharing**: PNG files are lighter in size and more convenient to share with patients or non-medical professionals.
- **Publications/Reports**: When medical images are needed for reports or publications, converting DICOM to PNG allows easy embedding into documents.


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

## Example

If your folder structure looks like this:
    /path/to/dicom/folder ├── file1.dcm ├── file2.dcm └── subfolder └── file3.dcm


After running the script, all PNG files will be saved in the output folder you specify.

## Script Details

- The script normalizes pixel intensity values from the DICOM files to a range of 0-255 for proper conversion to PNG.
- Each `.dcm` file will be saved as a `.png` file with the same name in the specified output folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to improving this script!

## Contact

If you have any questions, feel free to reach out via GitHub issues.

---

Happy converting! 😊

