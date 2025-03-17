from PIL import Image
import os

input_folder = "/gdrive/MyDrive/Dataset/good"
output_folder = "/gdrive/MyDrive/Resized1/good"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Resize all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add more extensions if needed
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            img_resized = img.resize((299, 299))
            img_resized.save(os.path.join(output_folder, filename))
print("Good images resized successfully!")

input_folder = "/gdrive/MyDrive/Dataset/bad"
output_folder = "/gdrive/MyDrive/Resized1/bad"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Resize all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add more extensions if needed
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            img_resized = img.resize((299, 299))
            img_resized.save(os.path.join(output_folder, filename))
print("Bad images resized successfully!")
