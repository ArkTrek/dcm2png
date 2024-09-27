# DICOM to PNG Converter

This repository contains a Python script that converts DICOM (.dcm) files into PNG format. The script traverses through a folder and its subfolders, identifies all `.dcm` files, and converts them to `.png` files. All the PNG files are saved in a single output folder.

## Features

- Converts DICOM files (.dcm) to PNG (.png).
- Processes DICOM files from a folder and all its subfolders.
- Outputs all PNG files to a single specified folder.
- Normalizes pixel intensity values for proper display in PNG format.

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

