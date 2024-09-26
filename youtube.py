

"""
def download_video(url, filePath_save):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_streams = streams.get_highest_resolution()
        high_streams.download(output_path=filePath_save)
        print("Should be okay")
    except Exception as e:
        print(e)

url = "https://www.youtube.com/watch?v=BVP_elhMz-A"
filePath_save = "/Users/denizsivas/VS_code"

download_video(url, filePath_save)
"""

"""
yt = YouTube("https://www.youtube.com/watch?v=BVP_elhMz-A")
yt.streams.get_highest_resolution().download()
"""

import yt_dlp

def download_video(url, filePath_save):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{filePath_save}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = "https://www.youtube.com/watch?v=BVP_elhMz-A"
filePath_save = "/Users/denizsivas/VS_code"

download_video(url, filePath_save)
