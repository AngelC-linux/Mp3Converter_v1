# mp3Converter
# Jose Angel Cardona García
# Personal Proyect

import pytube
import os
import shutil
import eyed3
from moviepy.editor import VideoFileClip


def mp3_format(filename):
    archive = VideoFileClip(filename)
    archive.audio.write_audiofile(filename[:-4] + ".mp3")
    archive.close()

def video_resolution(url, quality = 'low'):
    video = pytube.YouTube(url)
    mp4 = video.streams.filter(res=quality).first()
    mp4.download()

    return mp4.default_filename

def insert():
    print("Paste the link here: ")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"MESSAGE: The file '{filename}' was removed\n")
    except OSError as e:
        print(f"---> WARNING!!!: Error deleting the file'{filename}': {e} !!!\n\n")

def mv_files():
    actual_path = "/Add/your/path/downloaded/file"
    destination_path = "/Add/your/path/where/you/want/move/the/file"
    files = os.listdir(actual_path)
    for filename in files:
        if filename[-4:] == '.mp3':
            file_path = os.path.join(actual_path, filename)
            destination_file_path = os.path.join(destination_path, filename)
            shutil.move(file_path, destination_file_path)
            print(f"---> Moved '{filename}' to '{destination_path}'")

            audiofile = eyed3.load(destination_file_path)
            if audiofile.tag:
                title = audiofile.tag.title
                artist = audiofile.tag.artist
                album = audiofile.tag.album
                year = audiofile.tag.getBestDate()
                print(f"'{title}' by '{artist}'. Album: '{album}'. Year: {year}")



print("----------- MP3 Converter ----------------\n")

insert()
link = input()
print("Downloading...\n")
filename = video_resolution(link, quality='360p')
print("Converting...\n")
mp3_format(filename)
mv_files()
filename = filename[:-4]
delete_file(filename + ".mp4")
