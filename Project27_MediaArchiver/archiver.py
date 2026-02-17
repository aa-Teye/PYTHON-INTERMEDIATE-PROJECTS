import yt_dlp

def download_media(url, mode):
    # Configuration based on user choice
    if mode == '1': # High Quality Video
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
    else: # Audio Only (MP3)
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n[🚀] Starting download...")
            ydl.download([url])
            print(f"\n[✔] Successfully archived!")
    except Exception as e:
        print(f"\n[✘] Error: {e}")

if __name__ == "__main__":
    print("--- PROJECT 27: MEDIA ARCHIVER ---")
    video_url = input("Paste the Video URL: ")
    print("\nSelect Download Mode:")
    print("1. Full Video (MP4)")
    print("2. Audio Only (MP3)")
    
    choice = input("\nChoice (1 or 2): ")
    download_media(video_url, choice)