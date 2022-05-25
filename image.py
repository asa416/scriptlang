from tkinter import *

class ImageButton(Button):
    def __init__(self, parent, width=100, height=50, filename = None):
        super().__init__(parent)
        self.width = width
        self.height = height
        if filename:
            self.setImage(filename)

    def setImage(self, filename):
        from PIL import Image, ImageTk

        im = (Image.open(filename))
        
        im = im.resize((self.width,self.height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        self.configure(image = img)
        self.image = img

def change_img():
    print('adfadsfadsf')

if __name__ == '__main__':

    window = Tk()
    imageLabel = ImageButton(window)
    imageLabel.setImage('images/x.gif')
    imageLabel.pack()

    window.mainloop()