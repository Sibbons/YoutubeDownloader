import tkinter as tk
from pytube import YouTube
from pytube import Playlist
import os

def get_mp4(url):
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
            ytd = YouTube(video_url).streams.filter(adaptive=True).first().download()
            os.rename(ytd.streams.first().default_filename, f'{ytd.title}.mp3')
        except Exception as e:
            pass


def convert_to_mp3():
    curr_dir = os.getcwd()    
    for index, dirs, files in os.walk(curr_dir):
        for file in files:
            if file.endswith(".mp4"):
                base = os.path.splitext(file)[0]
                os.rename(file, base +'.mp3') 


def getURL(): 
    url = entry1.get()
    
    label3 = tk.Label(root, text= 'Your videos are downloading \n Please wait {}'.format(url))
    canvas1.create_window(200, 210, window=label3)
    get_mp4(url)
    convert_to_mp3()

root= tk.Tk()
root.title('Youtube to MP3')

canvas1 = tk.Canvas(root, width = 400, height = 130,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Download the mp3 files from youtube (playlists included)')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 30, window=label1)

label2 = tk.Label(root, text='Enter URL')
label2.config(font=('helvetica', 8))
canvas1.create_window(85, 60, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(220, 60, width = 200, window=entry1)    


button1 = tk.Button(text='Submit', command=getURL, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 95, window=button1)

root.mainloop()


