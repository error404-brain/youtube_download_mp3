import yt_dlp

video_url = 'https://www.youtube.com/watch?v=u4JqHoSMbbg'

# Set options to download audio only
ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in the 'downloads' folder with the video title
    'format': 'bestaudio/best',  # Select best audio format
}

# Download the audio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")
