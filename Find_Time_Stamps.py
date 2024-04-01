import requests
import re

def findTimeStamps(link):
    page = requests.get(link)

    pattern = r'{"startMillis":"(\d+(?:\.\d+)?)","durationMillis":"(\d+(?:\.\d+)?)","intensityScoreNormalized":(\d+(?:\.\d+)?)}'

    matches = re.findall(pattern, page.text)


    intensity_max = 0.0

    #Default case it returns start of video
    most_watched_part = 0

    for match in matches:
        start_millis, duration_millis, intensity_score = match
        #Search for most rewatched part of video and convert data into float
        if(float(intensity_score) > intensity_max and float(intensity_score) < 1):
            most_watched_part = float(start_millis)
            intensity_max = float(intensity_score)

    print("most_watched_part " + str(most_watched_part / 1000) + "s")
    return int(most_watched_part/1000)
