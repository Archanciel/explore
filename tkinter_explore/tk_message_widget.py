from tkinter import *
import time
  
root = Tk() 
root.geometry("500x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.grid(row=1, column=1) 
    
msg = Message( root, aspect=400)   
    
msg.grid(row=2, column=0, columnspan=2, padx=2)   
  
msgText = 'coucou'
msg.configure(text=msgText)
root.update()

for i in range(5):
	time.sleep(1)
	msgText = msgText + ' ' + 'coucou'
	msg.configure(text=msgText)
	root.update()
	
#root.mainloop() 
