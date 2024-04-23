import os
import tkinter as tk
from tkinter import ttk
import requests
from threading import Thread
import subprocess

class DownloadAndUnzipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Download File App")
        self.root.geometry("400x150")
        
        self.progress_label = ttk.Label(root, text="Progress:")
        self.progress_label.pack()
        
        self.progressbar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300)
        self.progressbar.pack()
        
        self.download_button = ttk.Button(root, text="Download File", command=self.download_file)
        self.download_button.pack()
    
    def download_file(self):
        download_url = "https://docs.google.com/forms/u/1/d/12SJ91wIuYTPWUigr2fHaYhflrzM6UHe6AV33fyWZQi4/downloadresponses?tz_offset=-14400000&sort_by_timestamp=true"
        download_path = "H:/Skua Stats Decompile/Skua Script Statistics Form v2.csv.zip"
        
        self.progress_label.config(text="Downloading...")
        self.progressbar['value'] = 0
        self.root.update_idletasks()
        
        download_thread = Thread(target=self.download, args=(download_url, download_path))
        download_thread.start()
        
        # Wait for the download thread to finish
        download_thread.join()
        
        self.progress_label.config(text="Download complete")
        
        # Open the downloaded file
        subprocess.Popen(['start', download_path], shell=True)

    def download(self, url, file_path):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        with open(file_path, 'wb') as file:
            for data in response.iter_content(block_size):
                file.write(data)
                self.progressbar['value'] += block_size
                self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloadAndUnzipApp(root)
    root.mainloop()
