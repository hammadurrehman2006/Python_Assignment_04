import tkinter as tk
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.eraser = None

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)

    def moveto(self, item, x, y):
        self.canvas.coords(item, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

    def get_mouse_x(self):
        return self.root.winfo_pointerx() - self.root.winfo_rootx()

    def get_mouse_y(self):
        return self.root.winfo_pointery() - self.root.winfo_rooty()

    def wait_for_click(self):
        self.root.update_idletasks()
        self.root.update()

    def get_last_click(self):
        # Tkinter doesn't provide a direct way to get the last click position
        # We'll use a workaround by binding a click event to a function
        self.click_x = None
        self.click_y = None

        def on_click(event):
            self.click_x = event.x
            self.click_y = event.y
            self.root.quit()

        self.canvas.bind("<1>", on_click)
        self.root.mainloop()
        return self.click_x, self.click_y

def erase_objects(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(last_click_x, last_click_y, last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE, 'pink')
    canvas.eraser = eraser

    def update():
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        canvas.root.after(50, update)

    update()
    canvas.root.mainloop()

if __name__ == '__main__':
    main()