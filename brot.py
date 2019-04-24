import time
import keyboard
import mouse
import random
from threading import *
from tkinter import *

class botty_mc_botface:

    def __init__(self):
        self.running = 1
    def terminate(self):
        self.running = 0

    def action(self):
        mouse.press(mouse.LEFT)
        time.sleep(1)
        mouse.release(mouse.LEFT)
        time.sleep(1)
        keyboard.press("R")
        time.sleep(1)
        keyboard.release("R")
        keyboard.press("E")
        time.sleep(1)
        keyboard.release("E")

    def botting(self):
        self.running = 1
        start = time.time()
        while self.running:
            time.sleep(1)
            print("running")
            if time.time() > start+30:
                self.action()
                start = time.time()

class App:
  def __init__(self, master):

    self.bot = botty_mc_botface()

    self.botthread = Thread(target=self.bot.botting)
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="Start Bot",
                         command=self.botthread.start)
    self.slogan.pack(side=LEFT)

    self.slogan = Button(frame,
                         text="End Bot",command=self.bot.terminate)
    self.slogan.pack(side=LEFT)

root = Tk()
app = App(root)
root.mainloop()


























