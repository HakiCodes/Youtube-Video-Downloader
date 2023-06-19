from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeStream = youtubeObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        youtubeStream.download()
    except:
        print("An error has occurred!!!!!!!!!!!!!")
    print("download complete")
        
link = input("Enter URL here: ")
Download(link)
