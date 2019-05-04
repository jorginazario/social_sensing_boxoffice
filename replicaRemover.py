def readMoviesWanted(fileName):
    movieList = []
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movie_name = lis[0].rstrip()
        movieList.append(movie_name)  
    return set(movieList)

def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[1].rstrip()
    return movieDict

def writeToFile (dictionary):
    filename = "FinalList.txt"
    output = open(filename, 'w')
    for key in dictionary:
        output.write(str(key+ ','+ dictionary[key]))
        output.write('\n')
    output.close

def get_key(val,my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
    return False 

listfromRatings = readMoviesWanted("newFinalMovieRatings.txt") # this is movie list we want popularity on
newmovieDict = readMovieList("newMovielist.txt") # this is dictionary with data 
newmovieDictcheck = readMovieList("newMovielistCheck.txt") #this is dictionary with data

print (len(listfromRatings))
print(len(newmovieDict))
print(len(newmovieDictcheck))

finaldict={}

for title in listfromRatings:
    if (get_key(title,newmovieDict)):
        finaldict[get_key(title,newmovieDict)] = title
    elif (get_key(title,newmovieDictcheck)):
        finaldict[get_key(title,newmovieDictcheck)] = title
    else:
        print(title)

#dont forget this or else it will screw u lol
writeToFile(finaldict)

