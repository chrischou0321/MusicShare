import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
requestContent = request.content
requestSoup = BeautifulSoup(requestContent, "html.parser")
for element in requestSoup.find_all('a', {"rel": "spf-prefetch"}):
    videoTitle = element.get('title')
    print(videoTitle);