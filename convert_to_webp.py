import os
from PIL import Image, UnidentifiedImageError
from config import INPUT_IMAGES_DIR, WEBP_IMAGES_DIR, WEBP_QUALITY

def convert_to_webp(input_path, output_path, quality):
    """
    Converts all images in the input directory to WebP format 
    and saves them to the output directory while preserving 
    original structure and filenames.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                # Define input and output file paths
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_path).replace("\\", "/")
                webp_file = os.path.join(output_path, relative_path)
                webp_file = webp_file.rsplit('.', 1)[0] + ".webp"

                # Ensure the directory for the output file exists
                os.makedirs(os.path.dirname(webp_file), exist_ok=True)

                try:
                    # Open the input image and save it as WebP
                    with Image.open(input_file) as img:
                        print(f"Processing: {input_file}")
                        img = img.convert("RGB")  # Ensure RGB format
                        img.save(webp_file, "WEBP", quality=quality)
                        print(f"Converted: {input_file} -> {webp_file}")
                except UnidentifiedImageError:
                    print(f"Error: {input_file} is not a valid image file or is corrupted.")
                except Exception as e:
                    print(f"Unexpected error processing {input_file}: {e}")

if __name__ == "__main__":
    convert_to_webp(INPUT_IMAGES_DIR, WEBP_IMAGES_DIR, WEBP_QUALITY)
