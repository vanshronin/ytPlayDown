import yt_dlp
import os  # ← add this

# Make folder if it doesn't exist
folder_name = "phonkPlay"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

playlist_url = input("Enter YouTube playlist URL: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{folder_name}/%(playlist_index)s - %(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Done ✅")