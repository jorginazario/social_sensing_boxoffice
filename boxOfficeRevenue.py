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
        movieDict[lis[0]] = lis[1]
    return movieDict

def getMovieEarning(movieDict):
    earningDict = {}
    for key in movieDict.keys():
        movieName = movieDict[key]
        movieName = str(movieName).rstrip()
        queryString = url+movieName
        response = requests.get(queryString)
        html = response.text
        checkForNone = re.search(regex2, html)
        if (response.status_code == 200 and checkForNone == None):
            m = re.findall(regex,html)
            if (len(m)>0):
                earningText = m[1]
                filterNum = re.findall(regex3,earningText)
                #print (filterNum)
                if (len(filterNum)>0):
                    a=filterNum
                    #filterNum = re.findall(regex3,earningText)[0]
                    # print("In that IF")
                else:
                    filterNum = 0
            else:
                filterNum = "N/A" 
            finalRev = ""
            if (len(filterNum) >0):
                for i in range(len(filterNum)):
                    #print("Harry")
                    if (i == 0):
                        continue
                    else:
                        #print(filterNum[i])
                        finalRev+= str(filterNum[i])
            if (finalRev != ""):
                earningDict[movieName] = int(finalRev)
            else:
                earningDict[movieName] = 0
    return earningDict

def writeToFile(tweetDict):
    j = json.dumps(tweetDict)
    f = open("boxEarnings.json", 'w')
    f.write(j)
    f.close()

movieDict = readMovieList('movielist.txt')
earningDict = getMovieEarning(movieDict)
writeToFile(earningDict)
print(earningDict)