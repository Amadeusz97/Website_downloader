import os, sys
import urllib.parse
import validators
import requests
import datetime

print("Number of arguments: ", len(sys.argv))
print("Arguments: ", sys.argv)

url = "https://wp.pl"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website adress: ", url)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
print("Current working dir: ", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)
if validFlag:
    print("URL:", url, "is valid")
else:
    print("URL:", url, "is invalid")
    raise Exception("Bad URL")

response = requests.get(url, allow_redirects=True)
if response.ok:
    print("Server ok from response for url:", url)
    now = datetime.datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateString)
    fileName = "./websites/" + parsedUrl.netloc + " " + dateString + ".html"
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
