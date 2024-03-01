import cv2

def clockwise90(image):
    return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

def anticlockwise90(image):
    return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

def clockwise180(image):
    return cv2.rotate(image, cv2.ROTATE_180)

def anticlockwise180(image):
    return cv2.rotate(image, cv2.ROTATE_180)

def default():
    print("Invalid choice")

if __name__ == "__main__":
    image_path = "./dog.png"
    image = cv2.imread(image_path)

    if image is not None:
        print("Enter your choice:")
        print("1: Clockwise 90\n2: Anti Clockwise 90\n3: Clockwise 180\n4: Anti Clockwise 180")

        choice = int(input())

        switch_dict = {
            1: clockwise90,
            2: anticlockwise90,
            3: clockwise180,
            4: anticlockwise180,
        }

        rotated_image = switch_dict.get(choice, default)(image)

        # Display the input and output images
        cv2.imshow("Original Image", image)
        cv2.imshow("Rotated Image", rotated_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("***Image reading failed***")
