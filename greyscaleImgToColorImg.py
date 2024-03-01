import cv2

# Specify the path to your grayscale image
grayscale_image_path = "./tree.jpg"

# Read the grayscale image
grayscale_image = cv2.imread(grayscale_image_path, cv2.IMREAD_GRAYSCALE)

if grayscale_image is not None:
    if grayscale_image.ndim == 2:
        # Apply a colormap to create a pseudo-color representation
        color_image = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_JET)

        # Display the grayscale image
        cv2.imshow("Grayscale Image", grayscale_image)

        # Display the pseudo-color image
        cv2.imshow("Pseudo-Color Image", color_image)

        # Wait for a key event (0 means wait indefinitely until a key is pressed)
        cv2.waitKey(0)

        # Close all OpenCV windows
        cv2.destroyAllWindows()
    else:
        print("Error: The input image is not grayscale.")
else:
    print(f"Error: Unable to read the image from {grayscale_image_path}")
