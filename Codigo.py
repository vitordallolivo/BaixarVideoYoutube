import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube


def choose_destination_folder():
    folder_path = filedialog.askdirectory()
    return folder_path


def download_video():
    try:
        video_url = video_url_entry.get()
        destination_folder = choose_destination_folder()
        if not video_url:
            messagebox.showwarning("Warning", "Please enter a valid YouTube video URL.")
            return
        if not destination_folder:
            return
        youtube = YouTube(video_url, on_progress_callback=progress_callback)
        video = youtube.streams.get_highest_resolution()
        video.download(destination_folder)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def download_audio():
    try:
        video_url = video_url_entry.get()
        destination_folder = choose_destination_folder()
        if not video_url:
            messagebox.showwarning("Warning", "Please enter a valid YouTube video URL.")
            return
        if not destination_folder:
            return
        youtube = YouTube(video_url, on_progress_callback=progress_callback)
        audio = youtube.streams.get_audio_only()
        file_path = audio.download(destination_folder)
        base, ext = os.path.splitext(file_path)
        new_file_path = base + '.mp3'
        os.rename(file_path, new_file_path)
        messagebox.showinfo("Success", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_label.config(text="Downloading... {:.2f}%".format(percentage))


root = tk.Tk()
root.geometry("300x150")
root.title("YouTube Downloader")

video_url_label = tk.Label(root, text="Enter YouTube video URL:")
video_url_label.pack()

video_url_entry = tk.Entry(root)
video_url_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

video_button = tk.Button(button_frame, text="Download Video", command=download_video)
video_button.pack(side=tk.LEFT, padx=5)

audio_button = tk.Button(button_frame, text="Download Audio", command=download_audio)
audio_button.pack(side=tk.LEFT, padx=5)

progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
