from pytube import YouTube

def download_video(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print('Error!')
    print('Successfully!')

link = input('Type link: ')
download_video(link)
