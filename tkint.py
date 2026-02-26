import tkinter as tk

root = tk.Tk()

root.title("windo")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

instruction = tk.Label(root, text="don't press the red button").pack()
red_button = tk.Button(root, bg = "red", text= "press me!").place(x=125, y=50)
root.mainloop