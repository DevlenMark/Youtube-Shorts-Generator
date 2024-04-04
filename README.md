# Youtube Shorts Generator
 
## Generates Youtube Shorts like video files by finding most rewatched part of a video and cutting that video on top of Minecraft Parkour. 

This project uses Youtube API, PyTube, and MoviePy in order to create youtube short's from any youtube video. It uses Youtube API to find the link of a search. Then it uses PyTube to download that video. Then I used request to get the html of the Youtube Link, and found all that matched a certain pattern that relates to the heatmap feature in Youtube. I saved all of those values, and found the most rewatched part of the video. Then with MoviePy, I cut the video from that part, added random minecraft Parkour, and downloaded the final video.

## Installation
This program requires you to set up an [Youtube API key](https://www.youtube.com/results?search_query=how+to+set+up+youtube+api+key), but not OAuth. 
Use the package manager [pip](https://pypi.org/project/pip/) to install these packages:
- Google API Client
- PyTube
- MoviePy
- Open-CV Python

## Usage
In your IDE of choice, call the method:
```python
videoShortGenerator('#Insert your YT Link of Search in here')
```

## Examples







