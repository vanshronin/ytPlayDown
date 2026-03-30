import yt_dlp
import os

# Folder to save MP3s
folder_name = "bhaktiPlay"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Playlist URL
playlist_url = input("\nPaste YouTube Playlist URL: ")

# YT-DLP options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{folder_name}/%(playlist_index)s - %(title)s.%(ext)s',
    'noplaylist': False,       # allow full playlist
    'ignoreerrors': True,      # skip problematic videos
    'extract_flat': False,     # download actual videos, not just metadata
    'yes_playlist': True,      # force playlist download
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [        # optional: shows which video is being downloaded
        lambda d: print(f"Downloading: {d['filename']}") if d['status'] == 'downloading' else None
    ]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("\nAll songs downloaded to bhaktiPlay ✅")
