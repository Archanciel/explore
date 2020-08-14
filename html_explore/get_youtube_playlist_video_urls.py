import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
video = ""


yt_url = 'https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L'

with ydl:
    result = ydl.extract_info \
    (yt_url,
    download=False) #We just want to extract the info

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']

        #loops entries to grab each video_url
        for i, item in enumerate(video):
            video = result['entries'][i]
            print(video['webpage_url']) 
            