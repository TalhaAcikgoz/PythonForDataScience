from numpy import array
import cv2


def ft_load(path: str) -> array:
    """ Loads the picture in path. """
    try:
        assert path[-3:] == "jpg" or path[-4:] == "jpeg", \
            "Image type need to be jpg or jpeg."
        assert path != "", \
            "Image path can not be empty."
        open(path, "r")
        img = array(cv2.imread(path))
        return img
    except FileNotFoundError as e:
        print(e)
        exit(e.errno)
    except AssertionError as e:
        print(e)
        exit(1)
