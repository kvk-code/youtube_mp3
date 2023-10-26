import yt_dlp as youtube_dl  # Change this line

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Provide the YouTube video URL to the function
download_audio('https://www.youtube.com/watch?v=C3lWwBslWqg')
