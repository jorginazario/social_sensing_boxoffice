#Written By: Harry Gebremedhin & Jorge Nazario 
#Connects with The Movie Database API and outputs a list of movies released in 2018
import requests
import json

API_KEY = "7417abbde348201c297bfac2fb122294"
page = ["1","2","3","4","5","6","7","8","9","10"] # chose 4 pages so that we have 80 movies to look at
URL = "https://api.themoviedb.org/3/discover/movie?api_key="+API_KEY+"&language=en-US&sort_by=popularity.desc"+"&page="

#function that calls the api and returns dictionary with id and movie title
def getMovieTitles():
    dictionary = {}
    #Looking at 4 result pages
    for number in page:
        movies = requests.get(URL+number)
        mList = json.loads(movies.text)["results"]
        for instance in mList:
            ID,title,popularity = str(instance["id"]), instance["title"],str(instance["popularity"])
            dictionary[ID] = title
    return dictionary

#functions that takes the resulting dictionary and writes it to a file
def writeToFile(dictionary):
    fileName = "newMovielistCheck.txt"
    outPut = open(fileName, 'w')
    for key in dictionary:
        outPut.write(str(key+","+dictionary[key]))
        outPut.write('\n')
    outPut.close()

movieDict = getMovieTitles()
writeToFile(movieDict)




