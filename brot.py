import time
import keyboard
import mouse
import random
time.sleep(10)
while True:
    mouse.press(mouse.LEFT)
    time.sleep(1)
    mouse.release(mouse.LEFT)
    time.sleep(1)
    keyboard.press("R")
    time.sleep(1)
    keyboard.release("R")
    time.sleep(random.randint(30,40))
    mouse.move(random.randint(0, 100), random.randint(0, 100), duration=1)
    keyboard.press("E")
    time.sleep(random.randint(30,40))
    keyboard.release("E")























