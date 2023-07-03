from pytube import YouTube
from . models import Audio
from yt_dlp import YoutubeDL
import random
import yt_dlp
import datetime
import ytdl
import subprocess
def download(link,request):
    # ytdl audio link
    output_directory = "main/static/main/audio/"
    output_format = output_directory+'%(title)s.%(ext)s'
    user =request.user

    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title', None)
        command = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', output_format, link]
        videos = subprocess.run(command, capture_output=True)
    if videos.returncode==0:
            vars=subprocess.run(['mv','ethos/'+str(video_title)+'.mp3','~/main/static/main/audio'])
            print(vars.returncode)
            # path='main/static/main/audio/'
            audio_objects_check = Audio.objects.filter(uploaded_by = user)
            audio_object_check = audio_objects_check.filter(url = link).first()
            if not audio_object_check:

                filename=str(video_title)+'.mp3'
                path='main/audio/'
                tempath=path +filename
                saveaudio=Audio()
                saveaudio.audioname = str(video_title)
                saveaudio.url = link
                saveaudio.audioFile=tempath
                saveaudio.uploaded_by_id = request.user.id
                saveaudio.url = link
                saveaudio.save()
                return saveaudio.id
            return audio_object_check.id
    else:
        return -1    

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







    # youtube_1=YouTube(link)
    # videos=youtube_1.streams.filter(only_audio=True)
    # if videos==videos1:
    #     print("yep")
    # videos[0].download(path,filename)