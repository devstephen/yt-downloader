from pytube import YouTube
from sys import argv
import pdb



link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)

pdb.set_trace()

print("Views", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(r"C:\Users\ndifreke\Desktop\Youtube")

