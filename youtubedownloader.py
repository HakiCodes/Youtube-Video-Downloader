from pytube import YouTube 

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred!!!!!!!!!!!!!")
        print("download complete")
        
link = input("Enter URL here: ")

Download(link)