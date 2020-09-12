from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
im = ImageGrab.grabclipboard()
Tk().withdraw()
path = asksaveasfilename(defaultextension='.png', filetypes=[('images', '*.png')], title='where save screen shot')

if im is not None:
    im.save(path, 'PNG')
    messagebox.showinfo("done!", "your image saved :)")
elif path == '':
    messagebox.showerror("cancel", "you cancel operation!")
else:
    messagebox.showerror("image doesn't exist", 'i cant find image in your clipboard!')
