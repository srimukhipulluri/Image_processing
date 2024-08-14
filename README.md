# Computer Vision Projects

This repository contains a collection of computer vision projects demonstrating various image transformation techniques and image processing methods. Each project includes code and examples for different image manipulations using popular libraries such as OpenCV and NumPy.

## Project Overview

### Affine Transformation
- **Description:** Applies an affine transformation to images, which includes translation, scaling, rotation, and shearing.
- **Key Concepts:** Matrix operations, linear transformations, and coordinate mapping.
- **Usage:** Run the `affine_transformation.py` script to apply affine transformations to sample images.

### Shear Transformation
- **Description:** Implements shear transformation to distort images by shifting pixels along the x or y axis.
- **Key Concepts:** Shear matrix, affine transformations, and image distortion.
- **Usage:** Execute the `shear_transformation.py` script to apply shear transformations.

### Image Restoration
- **Description:** Implements techniques to restore degraded images, such as deblurring and denoising.
- **Key Concepts:** Convolution, filtering, and noise reduction.
- **Usage:** Use the `image_restoration.py` script for restoring degraded images.

### Bit Plane Slicing
- **Description:** Performs bit plane slicing to visualize and analyze the contribution of individual bits to image data.
- **Key Concepts:** Bitwise operations, image encoding, and visualization.
- **Usage:** Run the `bit_plane_slicing.py` script to perform bit plane slicing on sample images.

### Histogram Equalization
- **Description:** Enhances image contrast using histogram equalization to improve visibility of features.
- **Key Concepts:** Histogram analysis, contrast adjustment, and image enhancement.
- **Usage:** Execute the `histogram_equalization.py` script to apply histogram equalization to images.

### Intensity Level Slicing
- **Description:** Applies intensity level slicing to enhance specific ranges of pixel intensity values in an image.
- **Key Concepts:** Thresholding, intensity manipulation, and image enhancement.
- **Usage:** Use the `intensity_level_slicing.py` script to apply intensity level slicing.

## File Structure

- `affine_transform.py` - Python script for affine transformation.
- `shear_transform.py` - Python script for shear transformation.
- `Restoration.py` - Python script for image restoration.
- `bit plane slicing.py` - Python script for bit plane slicing.
- `histogram_equalization.py` - Python script for histogram equalization.
- `intensity level slicing.py` - Python script for intensity level slicing.
- `README.md` - This file with project details.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy

You can install the necessary Python packages using pip:

```bash
pip install opencv-python numpy
