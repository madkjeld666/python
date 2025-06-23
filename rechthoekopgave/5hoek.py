import tkinter as tk

app = tk.Tk()
app.title("Rechthoek")
app.geometry("800x600")

canvas = tk.Canvas(app)
#canvas.create_rectangle(50, 0, 100, 50, fill='red')
canvas.create_polygon(50, 10, 100, 50, 75, 100, 50, -170, fill='red')
canvas.pack(expand= 1)
app.mainloop()