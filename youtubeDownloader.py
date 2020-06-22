import tkinter as tk
from pytube import YouTube
from pytube import Playlist
import os


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 150,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Download the mp3 file to a single youtube video or the entire playlist')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)

label2 = tk.Label(root, text='Enter URL')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 70, width = 200, window=entry1)



url = ""
def getURL(): 
    url = entry1.get()
    
    label3 = tk.Label(root, text= 'Your videos are downloading \n Please wait {}'.format(url))
    canvas1.create_window(200, 210, window=label3)

    url_list = []
    if "playlist" in url:
        playlist = Playlist(url)
        print("playlistSize: ",len(playlist.video_urls))
        url_list = list(playlist.video_urls)
    else:
        url_list.append(url)

    videos_missing = 0
    for video_url in url_list:
        try:
            ytd = YouTube(video_url).streams.filter(only_audio=True).first().download()
            os.rename(ytd.streams.first().default_filename, f'{ytd.title}.mp3')
        except Exception as e:
            pass
  



button1 = tk.Button(text='Submit', command=getURL, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 110, window=button1)

root.mainloop()


