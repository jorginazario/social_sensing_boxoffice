import json
import requests

URL = "https://api.themoviedb.org/3/movie/"
API_KEY = "?api_key=7417abbde348201c297bfac2fb122294&language=en-US"


def read(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        id_movie = lis[0]
        movie_title = lis[1].rstrip()
        movieDict[id_movie] = movie_title
    return movieDict

def getPopuarity(movieDict):
    popDict = {}
    for key in movieDict:
        url = URL+key+API_KEY
        response = requests.get(url)
        if (response.status_code == 200):
            response = json.loads(response.text)
            popularity = response["popularity"]
            popDict[movieDict[key]] = popularity
    return popDict

def writeToFile (dictionary):
    j = json.dumps(dictionary)
    f = open("moviePopularity.json", 'w')
    f.write(j)
    f.close()

movieDict = read("initialList.txt")
#print(movieDict)
popDict = getPopuarity(movieDict)
writeToFile(popDict)
