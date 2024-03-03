import cv2
import numpy as np

def convert_to_sketch(image_path):
    
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (111, 111), 0)
    inverted_blurred = cv2.bitwise_not(blurred)

    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

    cv2.imshow("Sketched image", sketch)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = "./dog.png"

    convert_to_sketch(input_image_path)
