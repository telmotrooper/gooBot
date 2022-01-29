from PIL import ImageGrab
from time import time


def save_image():
    # (0,0) is top-left
    initial_pos = {"x": 0, "y": 1080}
    screen_size = {"width": 1920, "height": 1080}
    box = (
        initial_pos["x"],
        initial_pos["y"],
        initial_pos["x"] + screen_size["width"],
        initial_pos["y"] + screen_size["height"])
    image = ImageGrab.grab(box)
    image.save(f"/tmp/goo_{int(time())}.png", "PNG")
