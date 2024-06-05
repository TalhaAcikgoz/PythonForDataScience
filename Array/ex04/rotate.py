import numpy as np
import cv2
from load_image import ft_load


def main(path: str):
    """ Main function. """
    img = ft_load(path)
    bw_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw_image = bw_image[90:490, 450:850]
    print(f"The shape of image is: {bw_image.shape}")
    print(bw_image.reshape((400, 400, 1)))
    col, row = bw_image.shape[0], bw_image.shape[1]
    tbw_image = np.zeros((row, col), dtype=np.uint8)
    for i in range(col):
        for j in range(row):
            tbw_image[j][i] = bw_image[i][j]
    print(f"New shape after Transpose: {tbw_image.shape}")
    print(tbw_image)
    cv2.imshow("Rakoon", tbw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        main("animal.jpeg")
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except Exception as e:
        print(f"Unexpected error {e}")
