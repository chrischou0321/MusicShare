import requests
import re
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
requestContent = request.content
requestSoup = BeautifulSoup(requestContent, "html.parser")

videoImageArea = requestSoup.find_all('img', {"alt": True, "width": True, "height": True, "onload": True,
                                                  "data-ytimg": True})
for element in requestSoup.find_all('a', {"rel": "spf-prefetch"}):
    # each image url's value
    videoValue = element.get('href').split("=")[1]
    imageUrl = re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(videoValue), str(videoImageArea))
    # cut no need prefix & suffix word
    imageUrl = str(imageUrl).strip("[]\"\'")
    imageUrl = imageUrl.replace("&amp;", "&")
    print(imageUrl)