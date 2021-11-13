from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

imeMape = ''

def odaberi_mapu():
    global imeMape

    try:
        imeMape = filedialog.askdirectory()
        labelPut.config(text = f'The video will be saved at: {imeMape}')

    except ValueError:
        labelPut.config(text = 'Map is incorrect!')

def preuzmi_video(videoUrl):
    urlString = videoUrl.get().strip()

    if(len(imeMape) > 0):

        try:
            yt = YouTube(urlString)
            yt = yt.streams.get_highest_resolution()
            yt.download(imeMape)

            labelPogresanUrl.config(text = f'Succesfully downloaded {yt.title}.')

        except ValueError:
            labelPogresanUrl.config(text = 'Entered URL is incorrect. You are dumb.')
    
    else:
        labelPut.config(text = 'Map for saving not chosen.')


root = Tk()

root.title('YouTube Downloader (Illegal download) V1.4')
root.configure(background = 'white')

ttk.Style().configure('TButton', padding = 6, relief = 'flat', background = 'white', foreground = 'red')

mainframe = ttk.Frame(root, padding = '3 3 12 12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

labelNaslov = ttk.Label(mainframe, text = 'YouTube Video Download (illegal) V1.4')
labelNaslov.configure(font = 'Minecraft 17', foreground = 'red')
labelNaslov.grid()

labelUrl = ttk.Label(mainframe, text = 'Enter URL in the box below!')
videoUrl = StringVar()

entryUrl = ttk.Entry(mainframe, width = 70, textvariable = videoUrl)
entryUrl.grid()

entryPut = ttk.Button(mainframe, width = 40, text = 'Choose saving destination...', command = odaberi_mapu)
entryPut.grid()

labelPut = ttk.Label(mainframe, text = 'Choose saving destination')

buttonDownloadVideo = ttk.Button(mainframe, text = 'Preuzmi video', command = lambda videoUrl = videoUrl: preuzmi_video(videoUrl))
buttonDownloadVideo.grid()

labelPogresanUrl = ttk.Label(mainframe, text = ' ')
labelPogresanUrl.grid()

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.mainloop()