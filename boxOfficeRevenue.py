#Written By: Harry Gebremedhin & Jorge Nazario 
#Program Crawls box office mojo website to get box office revenue for movie titles
import requests
import re
import json

url    = "https://www.boxofficemojo.com/search/?q="
regex  = '<td align="right"><font size="2"  face="verdana">.{20}'
regex2 = '<b>No Movies'
regex3 = '\d+'

def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[0]
    return movieDict

def getMovieEarning(movieDict):
    earningDict = {}
    for key in movieDict.keys():
        movieName = str(movieDict[key]).rstrip()
        queryString = url+movieName
        response = requests.get(queryString)
        html = response.text
        checkForNone = re.search(regex2, html) #seeing if boxoffice mojo couldn't find a movie title

        if (response.status_code == 200 and checkForNone == None):
            m = re.findall(regex,html)
            if (len(m)>0):
                if(len(m)>1):
                    earningText = m[1]
                else:
                    earningText = m[0]
                filterNum = re.findall(regex3,earningText)

                if (len(filterNum)>0):
                    a=filterNum
                else:
                    filterNum = 0
            else:
                filterNum = "N/A" 
            finalRev = ""
            if (len(filterNum) >0):
                for i in range(len(filterNum)):
                    if (i == 0):
                        continue
                    else:
                        finalRev+= str(filterNum[i])
            if (finalRev != ""):
                earningDict[movieName] = int(finalRev)
            else:
                earningDict[movieName] = 0
    return earningDict

def writeToFile(tweetDict):
    j = json.dumps(tweetDict)
    f = open("newBoxEarnings.json", 'w')
    f.write(j)
    f.close()

movieDict = readMovieList('newFinalMovieRatings.txt')
earningDict = getMovieEarning(movieDict)
writeToFile(earningDict)
print(earningDict)