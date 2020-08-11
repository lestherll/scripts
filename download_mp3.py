from __future__ import unicode_literals

from youtube_dl import YoutubeDL

#settings for download quality
download_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            
            'preferredcodec': 'mp3',    #ffmpeg converts video to mp3
            'preferredquality': '192',
        }],     
        #default_search allows the script to search videos without URL 
        'default_search': 'auto'	
        }  

def download(video=False):

        try:
            #user is prompted for input
            if video is False:
                video = input(" Enter video name or URL: ")

            #program downloads the video using the YoutubeDL object
            with YoutubeDL(download_options) as dl:
                dl.download([video])	

        except:
            print("Invalid")
            #video is set to false so that the script will prompt user for input
            video = False   

download()  #you can set video name or URL as a parameter too



