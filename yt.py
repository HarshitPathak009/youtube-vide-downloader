from pytube import YouTube

link = input("Enter the url of the video")

video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
print("Done")