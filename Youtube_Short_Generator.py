import Youtube_Link_Returner
import Find_Time_Stamps
import random
from moviepy.editor import VideoFileClip, clips_array, ColorClip, CompositeVideoClip

def videoShortGenerator(search):
    link = Youtube_Link_Returner.searchLinkOfVideo(search, 10)
    file_name = Youtube_Link_Returner.videoDownloader(link)
    start_time = Find_Time_Stamps.findTimeStamps(link)

    clipEditor(file_name, start_time)

def clipEditor(filename, start_time):
    # Set up YT Video
    yt_video = VideoFileClip(filename)
    #duration is 60 seconds
    end_time = start_time + 60
    #Makes sure that the end time is not longer thn the video itself
    if (end_time > yt_video.duration):
        end_time = yt_video.duration
    clip1 = VideoFileClip(filename).subclip(start_time, end_time)
    #1080 is the width of a phone screen resolution
    clip1_resized = clip1.resize(width=1080)

    # Set up Minecraft Parkcore
    mc_playtime = end_time - start_time
    mc_video = VideoFileClip(
        r'Youtube-Shorts-Generator/YT Videos/13 Minutes Minecraft Parkour Gameplay [Free to Use] [Map Download].mp4') #Replace with your file location of downloaded Minecraft Video
    #Finds random part of the video
    mc_start_time = random.randint(0, int(mc_video.duration - mc_playtime))
    clip2 = mc_video.subclip(mc_start_time, mc_start_time + mc_playtime)
    clip2_resized = clip2.resize(width=1080)

    # put the clips on top of eachother
    combined = clips_array([[clip1_resized], [clip2_resized]])

    #set up background
    background_clip = ColorClip(size=(1080, 1920), color=(0, 0, 0)).set_duration(combined.duration)

    #Put background into the clip
    final_clip = CompositeVideoClip([background_clip, combined.set_position(("center", "center"))])

    #Download clip
    final_clip.write_videofile('Youtube-Shorts-Generator/Final Short/final.mp4')

videoShortGenerator('https://www.youtube.com/watch?v=ozzoeMs9ks0')#Replace with link or search you wish for
