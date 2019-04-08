#Written By: Harry Gebremedhin & Jorge Nazario 
#Program Crawls the OMDB api getting all the different ratings of movies

import requests
import json


API_KEY = "3b466640"
URL = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="

def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[1]
    return movieDict


def getMovieRatings(movieDict):
    ratingDict = {}
    # print (movieDict)
    for key in movieDict:
        queryString = URL+movieDict[key]
        info = requests.get(queryString)
        if (info.status_code == 200):
            #changing text to a json dictionary
            info = json.loads(info.text)

            if ("Ratings" in info.keys()):
                ratings = info["Ratings"]
                r = len(ratings)-2
                rT = ratings[r]["Value"] # rotten tomatoes score
            else:
                rT = "N/A"

            if ("Metascore" in info.keys()):
                mT = info["Metascore"] # metacritic score
            else:
                mT = "N/A"

            if ("imdbRating" in info.keys()):
                imdbT = info["imdbRating"] # imdb score
            else:
                imdbT = "N/A"

            ratingDict[movieDict[key]] = (rT,imdbT,mT)
    return ratingDict

def writeToFile (dictionary):
    filename = "movieRatings.txt"
    output = open(filename, 'w')
    for key in dictionary:
        output.write(str(key+ ','+ dictionary[key][0] + ',' + dictionary[key][1] + ',' + dictionary[key][2]))
        output.write('\n')
    output.close

movieDict = readMovieList("movielist.txt")
ratingsDict = getMovieRatings(movieDict)
writeToFile(ratingsDict)




