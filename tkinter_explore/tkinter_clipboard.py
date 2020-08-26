try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk
    
r = Tk()
#r.withdraw()
clipboard_text = r.clipboard_get()
clipboard_text = clipboard_text.upper()
#r.clipboard_clear()
r.clipboard_append(clipboard_text)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()