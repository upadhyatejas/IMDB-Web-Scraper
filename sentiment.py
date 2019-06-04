from __future__ import print_function
from bs4 import BeautifulSoup as SOUP
from feels import feel
import re as regex
import requests as HTTP
import math 
def target(emotion):
    url = ""
    if emotion == "disgust":
        url = 'http://www.imdb.com/search/title?genres=musical&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "sad":
        url = 'http://www.imdb.com/search/title?genres=drama&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "trust":
        url = 'http://www.imdb.com/search/title?genres=western&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "anger":
        url = 'http://www.imdb.com/search/title?genres=family&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "fear":
        url = 'http://www.imdb.com/search/title?genres=sport&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "anticipation" or "enjoyment":
        url = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "surprise":
        url = 'http://www.imdb.com/search/title?genres=film_noir&amp;title_type=feature&amp;sort=moviemeter, asc'
    response = HTTP.get(url)
    data = response.text
    field = SOUP(data, "lxml")
    #REGEX EXTRACTION OF TITLES
    title = field.find_all("a", attrs = {"href" : regex.compile(r'\/title\/tt+\d*\/')})
    return title 
def analyse():
    emotion = input("Enter the emotion: ")
    sent=feel(emotion.lower())
    n=int(input("Enter no. of movie recommendations you want : "))
    print("Top",n," Recommended Movies : ")
    series = target(sent)
    count=0
    #print_function(series)
    for i in series :
        movie = str(i).split('>')
        if(len(movie) == 3):
            print(movie[1][:-3]) 
            count+=1
        if(count == n+1):
            break
analyse()
