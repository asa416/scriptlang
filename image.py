from tkinter import *

class ImageButton(Button):
    def __init__(self, parent, width=100, height=100, filenameOrUrl = None):
        super().__init__(parent, command=change_img)
        self.width = width
        self.height = height
        if filenameOrUrl:
            self.setImage(filenameOrUrl)

    def setImage(self, filenameOrUrl):
        from PIL import Image, ImageTk
        if filenameOrUrl.startswith('http'):
            from io import BytesIO
            import urllib.request

            url = filenameOrUrl
            try:
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()
            except urllib.error.URLError:
                print('urllib.error.URLError!')
                return

            im = Image.open(BytesIO(raw_data))
        
        elif filenameOrUrl:
            im = (Image.open(filenameOrUrl))
        
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