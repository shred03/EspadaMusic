import os
from yt_dlp import YoutubeDL

def audio_dl(url: str) -> str:
    cookie_path = os.path.join(os.path.dirname(__file__), "cookies.txt")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "prefer_ffmpeg": True,
        "noplaylist": True,  # <-- Force single video
        "cookiefile": cookie_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if not info:
            raise ValueError("Could not extract information from the URL.")
        if 'entries' in info:
            info = info['entries'][0]  

        file_path = os.path.join("downloads", f"{info['id']}.mp3")
        if os.path.exists(file_path):
            return file_path

        ydl.download([url])
        return file_path

