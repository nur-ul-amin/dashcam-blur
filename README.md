# Dashcam Plate Blurrer

A simple Python script to automatically blur specific regions (like license plates) in locally stored dashcam images using OpenCV. 

## Overview

This script takes an image path, reads the image, applies a Gaussian blur to predefined regions (Regions of Interest/ROIs), displays the result, and saves the protected image in the same directory as the original. 

It's essentially a local, desktop-friendly version of a Google Colab notebook designed for privacy protection.

## Prerequisites

You need Python installed on your system along with the following libraries:

- `opencv-python`
- `matplotlib`

You can install the required dependencies using pip:

```cmd
pip install opencv-python matplotlib
```

## How to Use

1. **Configure Image Path:**
   Open `blur_dashcam.py` in a text editor and update the `image_path` variable to point to the correct image file on your computer.
   ```python
   image_path = r"C:\path\to\your\image.jpg"
   ```

2. **Configure Blur Regions:**
   Update the `license_plate_rois` list with the coordinates for your specific image. 
   The format is `(x, y, width, height)`:
   ```python
   license_plate_rois = [
       (100, 200, 150, 50), # x=100, y=200, w=150, h=50
       (400, 180, 160, 55)  
   ]
   ```

3. **Run the Script:**
   Execute the script from your terminal:
   ```cmd
   python blur_dashcam.py
   ```

4. **View and Save:**
   - A matplotlib window will pop up showing the final image with the blurred areas.
   - The script will automatically save a new file named `protected_dashcam.jpg` in the same directory as the original image.

## Customization

- **Blur Intensity:** You can adjust the blur intensity by changing the kernel size in the `cv2.GaussianBlur` function. A larger kernel size (e.g., `(99, 99)`) creates a stronger blur effect. The current setting is `(51, 51)`.
