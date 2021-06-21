from pytube import YouTube
import pytube

# https://www.youtube.com/watch?v=PPu1ekDSKw8

link = str(input("\033[92m \n Enter youtube video link: \033[00m \n")).strip()

if len(link) == 0:
    print("\033[91m"+"----Give proper link----"+"\033[00m")
    exit()

try:
    yt = YouTube(link)
    title = yt.title

    print("\033[1m {} \033[00m".format(title))

    vid_filtered_yt = yt.streams.filter(progressive=True)
    aud_filtered_yt = yt.streams.filter(only_audio=True)
   
    type_file = int(input("\033[93m What you want to download? video = 1, audio = 2 \033[00m \n"))

    if type_file == 1:
        i = 1
        for f in vid_filtered_yt :
            print("\033[94m",i ," = " ,f.resolution ," ",f. filesize_approx/(1024*1024),"mb","\033[00m")
            i = i+1
        quality = int(input("\033[96m Enter resolution (index): \033[00m"))
        if quality > 0 and quality <= len(vid_filtered_yt) :
            video = vid_filtered_yt[quality-1]
            title = title + "_" + str(video.resolution)
            print("\033[92m ----Downloading is strated---- \033[00m")
            video.download(filename = title)
            print("\033[92m ----Downloading is completed---- \033[00m")
        else:
            print("\033[91m !!!!!!!!Something went wrong!!!!!!!! \033[00m")
    elif type_file == 2:
        i = 1
        for f in aud_filtered_yt :
            print("\033[94m",i ," = " ,f.abr ," ",f. filesize_approx/(1024*1024),"mb","\033[00m")
            i = i+1
        quality = int(input("\033[96m Enter bitrate : \033[00m"))
        if quality > 0 and quality <= len(aud_filtered_yt) :
            audio = aud_filtered_yt[quality-1]
            title = title + "_" + str(audio.abr)
            print("\033[92m ----Downloading is strated---- \033[00m")
            audio.download(filename = title)
            print("\033[92m ----Downloading is completed---- \033[00m")
        else:
            print("\033[91m !!!!!!!!Something went wrong!!!!!!!! \033[00m")
except pytube.exceptions.RegexMatchError:
    print("\033[91m Give Proper Link \033[00m")

except Exception as e:
    print("\033[91m !!!!!!!!Something went wrong!!!!!!!! \033[00m")
