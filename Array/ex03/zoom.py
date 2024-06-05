import numpy as np
import cv2
from load_image import ft_load


def ft_zoom(img: np.array):
    """ Zooming the image. """
    try:
        x, y = img.shape[0], img.shape[1]
        img = img[int(x/4)-90:int(x/4)+310, int(y/4)+190:int(y/4)+190+400]
        return img
    except Exception as e:
        print(f"An unexpected error occurred {e}")


def main(path: str):
    """ Main function. """
    img = ft_load(path)
    print(img)
    zoomed_img = ft_zoom(img)
    bw_image = cv2.cvtColor(zoomed_img, cv2.COLOR_BGR2GRAY)
    print(f"New shape after slicing: {bw_image.shape}")
    print(bw_image.reshape((400, 400, 1)))
    cv2.imwrite("ZoomedRakoon.jpeg", bw_image)
    cv2.imshow("Rakoon", bw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        main("animal.jpeg")
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except IndexError:
        pass
