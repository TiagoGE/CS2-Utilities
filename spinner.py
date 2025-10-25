import itertools
import threading
import time

class DotSpinner:
    def __init__(self, text="Loading", speed=0.5):
        # The frames of the animation
        self.frames = [".", " .", "  .", "   .", ""]
        self.spinner = itertools.cycle(self.frames)
        self.text = text
        self.speed = speed  # seconds per frame
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.animate)
        self.thread.start()

    def animate(self):
        while self.running:
            print(f"\r{self.text}{next(self.spinner)}", end="", flush=True)
            time.sleep(self.speed)

    def stop(self, final_text="Done!"):
        self.running = False
        if self.thread:
            self.thread.join()
        print(f"\r{final_text}{' ' * 10}")  # Clear leftover dots
