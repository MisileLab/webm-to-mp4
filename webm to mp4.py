import ffmpeg
import os

f = open('path.txt', 'r')
path = f.read()
f.close()

file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".webm")]
print(file_list_py)
for i in file_list_py:
    i = i.replace('.webm', '')
    stream = ffmpeg.input(f'{path}\\{i}.webm')
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.output(stream, f'{path}\\{i}.mp4')
    ffmpeg.run(stream)
    os.remove(f'{path}\\{i}.webm')