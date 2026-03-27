import cv2
def removeHair(img_org, img_gray, kernel_size=5, threshold=10, radius=3):

    # cross-shaped kernel for morphological operations (used to help detect thin dark structures)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    # perform the blackHat filtering on the grayscale image to find the hair contours
    blackhat = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)

    # segment the pixels where the difference between closing(image) and original image intensities is bigger than 10 
    _, mask = cv2.threshold(blackhat, threshold, 255, cv2.THRESH_BINARY)

    # fill in the white regions of the mask by using surrounding pixel information
    img_out = cv2.inpaint(img_org, mask, radius, cv2.INPAINT_TELEA)

    return blackhat, mask, img_out