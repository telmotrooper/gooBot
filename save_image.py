from PIL import ImageGrab
from time import time


def save_image():
    # (0,0) is top-left
    image = ImageGrab.grab()
    image.save(f"/tmp/goo_{int(time())}.png", "PNG")
