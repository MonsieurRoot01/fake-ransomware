from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# create window
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
root.title('Trollsomware')
root.config(bg='red')
root.iconphoto(False, tk.PhotoImage(file='padlock.png'))

# text YFHBE
text1 = Label(root, text="YOUR FILES HAS BEEN ENCRYPTED!", bg='white', font=("Courier", 55))
text1.pack(pady=50)

# display image
img = ImageTk.PhotoImage(file="padlock.png")
label = tk.Label(root, image=img)
label.pack()

# text unlock
text2 = Label(root, text="Enter the decryption key to find your files:", bg='red', fg='white', font=("Courier", 28))
text2.pack(pady=50)

# entry code
entryCode = tkinter.Entry(root, show="*", font=('Courier', 20), width=20,)
entryCode.pack(pady=20)

# btn
btn = tk.Button(root, text="Decrypt", font=('Courier', 50), width=15, bg='#222', fg="white", command=lambda: decrypt())
btn.pack(pady=50)

# decrypt script
key = 'test'

def decrypt():
    entryCodeGet = entryCode.get()
    if entryCodeGet == key:
        exit()
    else:
        text3 = Label(root, text="Try again", font=('Courier', 20))
        text3.pack()


root.mainloop()

