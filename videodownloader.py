import sys
import ssl
from tkinter import Tk, Entry, Button, Label, filedialog
from tkinter.font import Font
from PIL import Image, ImageTk
from pytube import YouTube

ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url, destination_folder):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(f"Downloading: {yt.title}")
        video.download(output_path=destination_folder)
        print(f"Download complete: {yt.title}")
        download_status_label.config(text="Done")
    except Exception as e:
        print(f"An error occurred: {e}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    destination_folder_entry.delete(0, 'end')
    destination_folder_entry.insert(0, folder_path)

def start_download():
    video_url = url_entry.get()
    destination_folder = destination_folder_entry.get()
    download_status_label.config(text="Downloading...")
    download_video(video_url, destination_folder)

root = Tk()
root.title("Video Downloader")

# Customize fonts
title_font = Font(family="Helvetica", size=24, weight="bold")
label_font = Font(family="Helvetica", size=14)
button_font = Font(family="Helvetica", size=12)



Label(root, text="Video URL:", font=label_font).grid(row=0, column=1, padx=10, pady=10)
url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Destination Folder:", font=label_font).grid(row=1, column=1, padx=10, pady=10)
destination_folder_entry = Entry(root, width=50)
destination_folder_entry.grid(row=1, column=2, padx=10, pady=10)

browse_button = Button(root, text="Browse", command=browse_folder, font=button_font)
browse_button.grid(row=1, column=3, padx=10, pady=10)

download_button = Button(root, text="Download", command=start_download, font=button_font)
download_button.grid(row=2, columnspan=3, padx=10, pady=10)

# Download status label
download_status_label = Label(root, text="", font=label_font)
download_status_label.grid(row=3, column=2, pady=10)

root.mainloop()
