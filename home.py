import tkinter as tk

# Create window
root = tk.Tk()
root.title("My House")
root.geometry("600x500")

# Create Canvas
canvas = tk.Canvas(root, width=600, height=500, bg="skyblue")
canvas.pack()

# 1. House body - rectangle
canvas.create_rectangle(
    150, 200, 450, 400,
    fill="lightyellow",
    outline="black"
)

# 2. Roof - triangle
canvas.create_polygon(
    120, 200,
    300, 80,
    480, 200,
    fill="red",
    outline="black"
)

# 3. Left window
canvas.create_rectangle(
    190, 240, 260, 310,
    fill="lightblue",
    outline="black"
)

# 4. Right window
canvas.create_rectangle(
    340, 240, 410, 310,
    fill="lightblue",
    outline="black"
)


# 5. Door
canvas.create_rectangle(
    270, 320, 330, 400,
    fill="brown",
    outline="black"
)

root.mainloop()
