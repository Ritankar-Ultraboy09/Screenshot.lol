import pyautogui
from PIL import Image, ImageGrab
import time 

def TakeScreenshot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    time.sleep(3)
    TakeScreenshot()

###DonebyRitankar



