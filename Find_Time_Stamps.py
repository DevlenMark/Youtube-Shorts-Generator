import requests
import re

def findTimeStamps(link):
    page = requests.get(link)

    #Pattern in HTML that is the heatmap function on youtube
    pattern = r'{"startMillis":"(\d+(?:\.\d+)?)","durationMillis":"(\d+(?:\.\d+)?)","intensityScoreNormalized":(\d+(?:\.\d+)?)}'

    #Gets all matches of this pattern
    matches = re.findall(pattern, page.text)


    intensity_max = 0.0

    #Default case it returns start of video
    most_watched_part = 0

    for match in matches:
        start_millis, duration_millis, intensity_score = match
        #Search for most rewatched part of video and convert data into float
        #Removes all rewatched that has intensity score of 1, as every video's start has a intensity score of 1
        if(float(intensity_score) > intensity_max and float(intensity_score) < 1):
            most_watched_part = float(start_millis)
            intensity_max = float(intensity_score)

    print("most_watched_part " + str(most_watched_part / 1000) + "s")
    return int(most_watched_part/1000)
