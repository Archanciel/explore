from tkinter import *
import tkinter.messagebox as msgb


root = Tk() # create a Tk root window

w = 600 # width for the Tk root
h = 300 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws - w) / 2
y = (hs - h) / 2

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.title('Order medicaments')

def on_sendMail():
    global entryform
    strng = entryform.get()
    if strng == '1':
        msgb.showinfo(message='You typed 1') # modif 3
    else:
        msgb.showinfo(message='Please type 1') # modif 4

entryform = Entry(root)
entryform.pack()
sendmail = Button(root, text="Send mail", command=on_sendMail)
sendmail.pack(side=BOTTOM)

root.mainloop() # starts the mainloop 