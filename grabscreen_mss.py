import numpy as np
import cv2
import time
from mss import mss
from PIL import Image


# Macbook have a bug about box's dimensions, can be just multiple of 16
# but this bug will be fix soon in the next release

def grab_screen():

    box = {"top": 45, "left": 0, "width": 1024, "height": 720}
    sct = mss()

    sct.get_pixels(box)

    # t = time.time()
    # image = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    # cv2.imshow('test', np.array(image))
    # print('fps: {}'.format(1/(time.time()-t)))
    # return np.array(image)

    while True:

        t = time.time()
        sct.get_pixels(box)
        image = Image.frombytes('RGB', (sct.width, sct.height), sct.image)

        # Could be useful in MAC OS
        # b, g, r = image.split()
        # image = Image.merge("RGB", (r, g, b))

        # Section displays screen & fps
        cv2.imshow('test', np.array(image))
        print('fps: {:.4}'.format(1/(time.time()-t)))

        # Why does this if statement impact anything unless I press 'q'?
        if cv2.waitKey(25) & 0xFF == ord('X'):
            cv2.destroyAllWindows()

        return np.array(image)
        # return cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
