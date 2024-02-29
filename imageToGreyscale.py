import cv2
import urllib.request
import numpy as np

def convert_to_grayscale(input_path):
    # Read the input image from a URL
    req = urllib.request.urlopen(input_path)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1)

    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = "https://unsplash.com/photos/assorted-color-buildings-near-red-boat-docked-on-port-during-daytime-I17LBNJq9q8"

    convert_to_grayscale(input_image_path)

    print("Conversion complete. Grayscale image displayed.")
