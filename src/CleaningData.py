import os
from PIL import Image
import numpy as np

image_dir = ".\Cleaned Dataset\imgs"   # Change to your actual image directory
mask_dir = ".\Cleaned Dataset\masks"   # Change to your actual mask directory

for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    mask_name = os.path.splitext(image_name)[0] + "_mask.png" 
    mask_path = os.path.join(mask_dir, mask_name)

    # Check if mask file exists (missing mask)
    if not os.path.exists(mask_path):
        print(f"Deleting {image_path} (missing mask)")
        os.remove(image_path)
        continue

    # Check if mask fits the image
    try:
        image = Image.open(image_path)
        mask = Image.open(mask_path)

        # Check size mismatch (unfitted mask)
        if image.size != mask.size:
            print(f"Deleting {image_path} (size mismatch: {image.size} vs {mask.size})")
            image.close()  
            mask.close()   
            os.remove(image_path)
            os.remove(mask_path)
            continue
        
        image.close() 
        mask.close()  

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        os.remove(image_path)
        if os.path.exists(mask_path):
            os.remove(mask_path)