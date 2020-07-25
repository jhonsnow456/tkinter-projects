from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

class Application:
    def __init__(self, root):
        root.title('QR Code Generator')

        self.label1 = Label(root, text='Enter Subject', font=('Helvetica', 12))
        self.label1.grid(row=0, column=0, sticky = N + S + E + W) 

        self.label2 = Label(root, text='Enter File Name', font=('Helvetica', 12))
        self.label2.grid(row=1, column=0, sticky = N + S + E + W) 

        self.subject = StringVar()
        self.subjectEntry = Entry(root, textvariable=self.subject, font=('Helvetica', 12))
        self.subjectEntry.grid(row=0, column=1, sticky= N + S + E + W)

        self.name = StringVar()
        self.nameEntry = Entry(root, textvariable=self.name, font=('Helvetica', 12))
        self.nameEntry.grid(row=1, column=1, sticky= N + S + E + W)

        self.cerateButton = Button(root, text='Create QR Code', font=('Helvetica', 12), width=15, command=self.generate)
        self.cerateButton.grid(row=0, column=3, sticky=N + S + E + W)

        self.notificationLabel = Label(root)
        self.notificationLabel.grid(row=2, column=1, sticky= N + S + E + W)

        self.subLabel = Label(root, text='')
        self.subLabel.grid(row=3, column=1, sticky=N + S + E + W)

        self.showButton = Button(root, text='Save as PNG', font=('Helvetica', 12), width=15, command=self.save)
        self.showButton.grid(row=1, column=3, sticky=N + S + E + W)

        # Making resposive layout
        self.totalRows = 3
        self.totalCols = 3

        for row in range(self.totalRows + 1):
            root.grid_rowconfigure(row, weight=1)
        for col in range(self.totalCols + 1):
            root.grid_columnconfigure(col, weight=1)

    # code generation
    def generate(self):
        if len(self.subject.get()) != 0:
            global myQr
            myQr = pyqrcode.create(self.subject.get())
            qrImage = myQr.xbm(scale=6)
            global photo
            photo = BitmapImage(data=qrImage)
        else:
            messagebox.showinfo('Error!', 'Please Enter the Subject')
        
        try:
            self.showCode()
        except:
            pass

    # code showing
    def showCode(self):
        global photo
        self.notificationLabel.config(image=photo)
        self.subLabel.config(text="Showing QR code for: " + self.subject.get())

    def save(self):
        # folder to save all code
        dir = pathl = os.getcwd() + '\\QR Codes'
        # create folder is it doesn't exist
        if not os.path.exists(dir):
            os.mkdir(dir)

        try:
            if len(self.name.get()) != 0:
                qrImage = myQr.png(os.path.join(dir, self.name.get() + '.png'), scale=6)
            else:
                messagebox.showinfo('Error!', 'File name cannot be Empty')
        except:
            messagebox.showinfo('Error!', 'Please generate the code first')


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
