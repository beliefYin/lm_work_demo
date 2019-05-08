import tkinter as tk
from login import Login

def exit(event):
	app.destroy()

app = tk.Tk()
app.title("某某软件")
app.bind('<Escape>' , exit)
Login(app)
app.mainloop()