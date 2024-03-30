import os
from dotenv import load_dotenv
from pytube import  YouTube
from pytube.exceptions import RegexMatchError
from googleapiclient.discovery import build


load_dotenv()
YT_Data_api_key = os.environ['YOUTUBE_DATA_API_KEY']
youtube = build('youtube', 'v3',  developerKey= YT_Data_api_key)
#Define a method that takes in a search query and returns the file path of a saved video
def videoDownloader(search):
    # where to save
    SAVE_PATH = r"C:\Users\devle\PycharmProjects\pythonProject\Youtube-Shorts-Generator\YT Videos"  # to_do

    # link of the video to be downloaded
    link = searchLinkOfVideo(search)

    try:
        # object creation using YouTube
        yt = YouTube(link)
    except:
        # to handle exception
        print("Connection Error")

        # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(progressive=True, file_extension='mp4')

    # get the video with the highest resolution
    d_video = mp4_streams[-1]

    try:
        # downloading the video
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except:
        print("Some Error!")




#Takes in a search query, search for the videos, and returns the link of top video
def searchLinkOfVideo(videoTitle):
   #Search for specific video with YouTube title
   print('Searching ' + videoTitle + "....")
   search_response = youtube.search().list(
       q=videoTitle,


       part='id,snippet',
       maxResults=1
   ).execute()


   # Extract video details from the response and prints it
   for search_result in search_response.get('items', []):
       video_id = search_result['id']['videoId']
       video_title = search_result['snippet']['title']
       video_description = search_result['snippet']['description']
       video_link = f"https://www.youtube.com/watch?v={video_id}"
       print(f"Video ID: {video_id}\nTitle: {video_title}\nDescription: {video_description}\nLink: {video_link}")


   return video_link


videoDownloader('han miserable')