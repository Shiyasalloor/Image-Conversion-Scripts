import cv2
import urllib.request
import numpy as np
from google.colab.patches import cv2_imshow

def convert_to_grayscale(input_path):
    try:
        # Read the input image from a file path
        image = cv2.imread(input_path)

        if image is None:
            print("Error: Unable to read the image from the provided file path.")
            return

        # Display the original image
        cv2_imshow(image)

        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display the grayscale image
        cv2_imshow(grayscale_image)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = "/content/dog.png"

    convert_to_grayscale(input_image_path)

    print("Conversion complete. Images displayed.")
