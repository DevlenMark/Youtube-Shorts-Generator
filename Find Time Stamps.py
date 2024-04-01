import requests
import re

link = "https://www.youtube.com/watch?v=iTDfI20gwGo"
page = requests.get(link)
print(page.text)

pattern = r'{"startMillis":"(\d+(?:\.\d+)?)","durationMillis":"(\d+(?:\.\d+)?)","intensityScoreNormalized":(\d+(?:\.\d+)?)}'

matches = re.findall(pattern, page.text)

for match in matches:
    start_millis, duration_millis, intensity_score = match
    print(f"Found match: startMillis={start_millis}, durationMillis={duration_millis}, intensityScoreNormalized={intensity_score}")



