import os
import tinify
from config import TINIFY_API_KEY, INPUT_IMAGES_DIR, COMPRESSED_IMAGES_DIR

# Set the API key for TinyPNG
tinify.key = TINIFY_API_KEY

def compress_images(input_path, output_path):
    """
    Compresses all images in the input directory using TinyPNG API
    and saves them to the output directory.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_path)
                output_file = os.path.join(output_path, relative_path)

                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                try:
                    print(f"Compressing: {input_file} -> {output_file}")
                    source = tinify.from_file(input_file)
                    source.to_file(output_file)
                except Exception as e:
                    print(f"Error compressing {input_file}: {e}")

if __name__ == "__main__":
    compress_images(INPUT_IMAGES_DIR, COMPRESSED_IMAGES_DIR)
