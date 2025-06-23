import tkinter as tk
from PIL import Image, ImageTk
import time

class MushroomAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=640, height=64, bg='white')
        self.canvas.pack()
        
        self.run_spritesheet = Image.open("Mushroom-Run.png")
        self.idle_spritesheet = Image.open("Mushroom-Idle.png")
        
        self.frame_width = 80
        self.frame_height = 64
        self.current_frame = 0
        self.is_running = True
        
        self.update_animation()
        self.root.bind("<space>", self.toggle_animation)
    
    def get_frame(self, spritesheet, frame):
        left = frame * self.frame_width
        upper = 0
        right = left + self.frame_width
        lower = self.frame_height
        frame_image = spritesheet.crop((left, upper, right, lower))
        return ImageTk.PhotoImage(frame_image)
    
    def update_animation(self):
        spritesheet = self.run_spritesheet if self.is_running else self.idle_spritesheet
        
        frame_image = self.get_frame(spritesheet, self.current_frame)
        self.canvas.delete("all")
        self.canvas.create_image(40, 32, anchor=tk.CENTER, image=frame_image)
        self.canvas.image = frame_image  # Houd een referentie bij
        
        self.current_frame = (self.current_frame + 1) % (spritesheet.width // self.frame_width)
        self.root.after(100, self.update_animation)  # Update elke 100ms
    
    def toggle_animation(self, event):
        self.is_running = not self.is_running
        self.current_frame = 0
        
root = tk.Tk()
app = MushroomAnimation(root)
root.mainloop()
