from pytube import YouTube
from . models import Audio
import random
import yt_dlp
import datetime
import ytdl
def download(link,request):
    # ytdl audio link
    youtube_1=YouTube(link)
    videos=youtube_1.streams.filter(only_audio=True)
    path='main/static/main/audio/'
    filename=youtube_1.title+ str(random.random()) +'.mp3'
    videos[0].download(path,filename)
    path='main/audio/'
    tempath=path +filename
    saveaudio=Audio()
    saveaudio.audioname = youtube_1.title
    saveaudio.audioFile=tempath
    saveaudio.uploaded_by_id = request.user.id
    saveaudio.url = link
    saveaudio.save()
    return saveaudio.id    

# URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

# ydl_opts = {
#     'format': 'm4a/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'm4a',
#     }]
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)