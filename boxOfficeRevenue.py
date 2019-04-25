#Written By: Harry Gebremedhin & Jorge Nazario 
#Program Crawls box office mojo website to get box office revenue for movie titles

import requests

url = "https://www.boxofficemojo.com/search/?q="

def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[1]
    return movieDict


def getMovieEarning(movieDict):
    for key in movieDict.keys():
        




movieDict = readMovieList("movielist.txt")