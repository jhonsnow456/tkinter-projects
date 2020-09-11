from tkinter import *
from pytube import YouTube
import os
import pygame

class Application:
    def __init__(self, root):
        self.root = root
        root.geometry('400x200')
        root.title('Youtube vedio Downloader Application')
        root.iconbitmap(r'.\res\YoutubeDownloader.ico') 

        # create the label widget to welcome user
        self.description = Label(root, text="Welcome!! to \n Youtube Downloader Application", font = 'Consolas 15 bold')
        self.description.pack()

        # progress message
        self.progress_message = StringVar()
        self.progress_message.set('Enter the link below')
        self.input1 = Entry(root, textvariable=self.progress_message, width=40)
        self.input1.pack(pady=10)

        # Copy youtube link here
        self.link = StringVar()
        self.input2 = Entry(root, textvariable=self.link, width=40)
        self.input2.pack(pady=10)

        # Click the button to download
        Button(root, text='Download Vedio', command=self.download).pack()

    # download function
    def download(self):
        try:
            self.progress_message.set('Downloading...')
            root.update()
            YouTube(self.link.get()).streams.first().download(os.getcwd() + '\\youtube')
            self.link.set('Vedio Dowloaded Sucessfully')
        except:
            self.progress_message.set('Check internet Connection or link')
            root.update()
            self.link.set('Enter correct link')
        
if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r".\res\xyz.mp3")
    pygame.mixer.music.play(-1)
    root.mainloop()
