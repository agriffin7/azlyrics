"""
Program: azlyrics.py
Author: Austin Griffin

This is a web scraping application that will allow users to look up lyrics
for songs. This program accepts the Musician/Band Name and the song that they
composed, and then outputs the lyrics.

"""
#Import Packages
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
while(True):
    #Ask user for Muscician
    singer = str(input("Please enter Musician/Singer's Name: "))
    singerHTML = singer.lower().strip().replace(" ","")

    #Ask user for song
    song = str(input("Please enter song Title: "))
    songHTML = song.lower().strip().replace(" ","")

    #set URL and request response
    url = 'http://azlyrics.com/lyrics/'+singerHTML+'/'+songHTML+'.html'
    response = requests.get(url)

    #Parse the HTML
    soup = BeautifulSoup(response.text,"html.parser")


    #Extract the lyrics
    lyrics = soup.findAll('div')[20]
                    
    #Display Information about the song
    print("-------------------------------------------------------------------------------")
    print("Artist: " + singer)
    print("Song: " + song)

    #Display Lyrics
    print(lyrics.get_text())
    print("-------------------------------------------------------------------------------")


    #stop from getting flagged as a spammer
    time.sleep(3)
