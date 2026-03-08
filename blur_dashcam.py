import cv2
import matplotlib.pyplot as plt
import os

# Step 1: Define the path to your image
image_path = r"C:\Users\LENOVO\Desktop\Desktop\F1\2009-Pagani-Zonda-R-001-1080.jpg"

if not os.path.exists(image_path):
    print(f"Warning: The path '{image_path}' does not exist.")
    print("Please check if 'Desktop\\Desktop' is a typo in the path.")

# Step 2: Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image. Please verify the image path is correct.")
else:
    # Step 3: Define license plate regions (x, y, width, height)
    # NOTE: Change these values to the actual license plate locations in your image
    license_plate_rois = [
        (100, 200, 150, 50), # Example 1
        (400, 180, 160, 55)  # Example 2
    ]

    # Step 4: Blur each license plate region safely
    height, width = image.shape[:2]
    for (x, y, w, h) in license_plate_rois:
        # Make sure ROI is inside image bounds
        if x < 0 or y < 0 or x + w > width or y + h > height:
            print(f"Skipping ROI {(x, y, w, h)} because it's outside the image boundaries.")
            continue
        
        roi = image[y:y+h, x:x+w]
        
        # Ensure ROI is valid
        if roi.size > 0:
            # You can increase the kernel size (e.g., (99, 99)) for more blur
            blurred_roi = cv2.GaussianBlur(roi, (51, 51), 0)
            image[y:y+h, x:x+w] = blurred_roi

    # Step 5: Save the protected image
    output_filename = "protected_dashcam.jpg"
    
    # Try to save in the same directory as the original image
    image_dir = os.path.dirname(image_path)
    if os.path.isdir(image_dir):
        output_path = os.path.join(image_dir, output_filename)
    else:
        # Fallback to current working directory
        output_path = output_filename
        
    cv2.imwrite(output_path, image)
    print(f"Saved protected image as {output_path}")
    
    # Step 6: Show the result
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Protected Dashcam Image (License Plates Blurred)")
    plt.axis('off')
    plt.show() # This will keep the image window open until you close it
