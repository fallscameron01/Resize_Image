"""
Contains the resize function that will resize an image stored in an ndarray by a scaling factor.
"""

import numpy as np

def resize(image, factor):
    """
    Function to resize images by a scaling factor.

    Parameters
    ----------
    image - ndarray - the image to resize
    factor - float - scaling factor to resize by

    Returns
    -------
    ndarray - the resized image
    """
    h, w, d = image.shape
    new_dimensions = np.floor((h*factor, w*factor, d))
    new_dimensions = tuple(new_dimensions.astype(int))
    newImg = np.resize(image, new_dimensions)
    
    for y in np.arange(0, new_dimensions[0]):
        for x in np.arange(0, new_dimensions[1]):
            try:
                newImg[y, x] = image[int(np.ceil(y / factor)), int(np.ceil(x / factor))]
            except:
                pass
    
    return newImg

if __name__ == "__main__":
    import cv2
    
    img = cv2.imread("images\\mars.jpg")
    
    cv2.imshow("Resized Image", resize(img, 1/3))
    cv2.waitKey(0)
    cv2.destroyAllWindows()