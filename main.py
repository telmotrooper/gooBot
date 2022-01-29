import time
from pynput.mouse import Button, Controller

config = {
    "slime1": (1759, 1776),
    "slime2": (1759, 1799),
    "target": "slime1"
}


def main():
    print("gooBot")
    interval = 5  # seconds

    start_time = time.time()

    while True:
        attack_slime()
        time.sleep(interval - ((time.time() - start_time) % interval))


def attack_slime():
    mouse = Controller()

    if config["target"] == "slime1":
        mouse.position = config["slime1"]
        config["target"] = "slime2"
    else:
        mouse.position = config["slime2"]
        config["target"] = "slime1"

    mouse.click(Button.left)


if __name__ == "__main__":
    main()
