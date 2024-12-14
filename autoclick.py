import pyautogui
from PIL import ImageGrab
import time

# Capture the selected screen part
x1 = 1041
x2 = 505
y1 = 1175
y2 = 530
screenshot = ImageGrab.grab(bbox=(x1, x2, y1, y2))
width, height = screenshot.size
# screenshot.show()
unsent_value = screenshot.getpixel((width/2, height/2))

def is_similar(tuple1, tuple2, threshold=5):
    # Check if the color of 2 pixels is close enough
    return all(abs(a - b) <= threshold for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    duration = 1 * 60
    # Record the start time
    start_time = time.time()
    # Loop until the elapsed time reaches the duration
    while time.time() - start_time < duration:
        time.sleep(0.5)
        screenshot = ImageGrab.grab(bbox=(x1, x2, y1, y2))
        screenshot_value = screenshot.getpixel((width/2, height/2))
        if is_similar(unsent_value, screenshot_value):
            click_x = (x1 + y1) / 2
            click_y = (x2 + y2) / 2
            pyautogui.click(click_x, click_y)
            time.sleep(0.5)
            continue
        else:
            break
