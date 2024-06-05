import numpy as np
import cv2
from numpy import array


def ft_invert(array) -> array:
    """ Invert the image colour. """
    if array is None:
        print("Array can not be empty.")
        exit(1)
    inverted_image = array.copy()
    inverted_image[..., 0] = 255 - inverted_image[..., 0]
    inverted_image[..., 1] = 255 - inverted_image[..., 1]
    inverted_image[..., 2] = 255 - inverted_image[..., 2]
    cv2.imwrite("InvertScape.jpeg", inverted_image)
    return inverted_image


def ft_red(array) -> array:
    """ Convert the image colour red. """
    if array is None:
        print("Array can not be empty.")
        exit(1)
    b, g, r = cv2.split(array.copy())
    b[:], g[:] = 0, 0
    cv2.imwrite("RedScape.jpeg", np.array(cv2.merge([b, g, r])))
    return np.array(cv2.merge([b, g, r]))


def ft_green(array) -> array:
    """ Convert the image colour green. """
    if array is None:
        print("Array can not be empty.")
        exit(1)
    b, g, r = cv2.split(array.copy())
    b[:], r[:] = 0, 0
    cv2.imwrite("GreenScape.jpeg", np.array(cv2.merge([b, g, r])))
    return np.array(cv2.merge([b, g, r]))


def ft_blue(array) -> array:
    """ Convert the image colour blue. """
    if array is None:
        print("Array can not be empty.")
        exit(1)
    b, g, r = cv2.split(array.copy())
    g[:] = 0
    r[:] = 0
    cv2.imwrite("BlueScape.jpeg", np.array(cv2.merge([b, g, r])))
    return np.array(cv2.merge([b, g, r]))


def ft_grey(array) -> array:
    """ Convert the image colour grey. """
    if array is None:
        print("Array can not be empty.")
        exit(1)
    grey = np.array(cv2.cvtColor(array, cv2.COLOR_BGR2GRAY))
    cv2.imwrite("GreyScape.jpeg", grey)
    return grey
