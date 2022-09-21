from pywinauto import Desktop, Application
import tkinter as tk
from tkinter import Button, filedialog, Text

application_root = tk.Tk(screenName="Automation Center")
application_root.title("Automation Center")

print(application_root.winfo_screen())

canvas = tk.Canvas(application_root, height=500, width=1000)
canvas.pack()

close_btn = Button(application_root, text="Close Automation Center", bg="teal")
close_btn.pack()
close_btn.a

application_root.mainloop()
