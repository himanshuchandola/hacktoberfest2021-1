#video downloader with python
from pytube import YouTube;

url = input('video url : ');
print('downloading..');

yt = YouTube(url);

video = yt.streams.get_by_resolution("720p");
video.download(output_path='D:/');
print('downloaded');
