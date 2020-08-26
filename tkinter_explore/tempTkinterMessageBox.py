import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
#w.withdraw()
w.after(1500, w.destroy) # Destroy the widget after 3 seconds
try:
	if messagebox.showinfo('formatkindlecode', 'Formatted code copied to clipboard'):
		w.destroy()
except:
	pass
