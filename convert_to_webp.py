from PIL import Image
import os
from urllib.parse import quote
from config import INPUT_IMAGES_DIR, WEBP_IMAGES_DIR, WEBP_QUALITY

def convert_to_webp(input_path, output_path, quality):
    """
    Converts all images in the input directory to WebP format 
    and saves them to the output directory with the specified quality.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_path).replace("\\", "/")
                
                # Encode file name to handle special characters
                relative_path_encoded = "/".join([quote(part) for part in relative_path.split("/")])
                webp_file = os.path.join(output_path, relative_path_encoded).replace(".jpg", ".webp").replace(".jpeg", ".webp").replace(".png", ".webp")

                os.makedirs(os.path.dirname(webp_file), exist_ok=True)

                try:
                    with Image.open(input_file) as img:
                        img = img.convert("RGB")
                        img.save(webp_file, "WEBP", quality=quality)
                        print(f"Converted: {input_file} -> {webp_file}")
                except Exception as e:
                    print(f"Failed to convert {input_file}: {e}")

if __name__ == "__main__":
    convert_to_webp(INPUT_IMAGES_DIR, WEBP_IMAGES_DIR, WEBP_QUALITY)
