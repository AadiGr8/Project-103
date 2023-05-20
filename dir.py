import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/AVINASH TODWAL/Downloads"
to_dir = "C:/Users/AVINASH TODWAL/Desktop/c103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("Hey, {event.from_dir} has been created")
        
    def on_deleted(self, event):
        print("{event.from_dir} has been deleted")

    def on_modified(self, event):
        print("{event.from_dir} has been modified")
        
    def on_moved(self, event):
        print("{event.from_dir} has been moved")

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,ext=os.path.splitext(event.src_path)

        for key,value in dir_tree.items():
            if ext in value:
                file_name=os.path.basename(event.src_path)
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name

                if os.path.exists(path2):
                    print("directory exist")
                    print("moving."+file_name)
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Making directory")
                    os.makedirs(path2)
                    print("moving."+file_name)
                    shutil.move(path1, path3)
                    time.sleep(1)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
    