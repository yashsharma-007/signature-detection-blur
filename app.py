import argparse
import os
from digiSignBlur import detect_and_blur_signatures


#python app.py path/to/image.jpg


#python app.py path/to/image.jpg --output_file path/to/processed_image.jpg




def main():
    parser = argparse.ArgumentParser(description="Detect and blur signatures in an image.")
    parser.add_argument('input_file', type=str, help="Path to the input image file")
    parser.add_argument('--output_file', type=str, default=None, help="Path to save the processed image")
    args = parser.parse_args()
    input_path = args.input_file
    output_path = args.output_file or f"processed_{os.path.basename(input_path)}"
    detect_and_blur_signatures(input_path, output_path)
    print(f"Processed image saved to {output_path}")
if __name__ == '__main__':
    main()
