__author__ = 'Savan Patel'
import urllib2 #need to open and see website data
from bs4 import BeautifulSoup #need to parse website data

#website url
url = 'http://www.imdb.com/search/title?languages=%C2%B7%C2%B7%C2%B7%C2%A0Common%20Languages%C2%A0%C2%B7%C2%B7%C2%B7&release_date=2010-01-01,2017&title_type=feature&user_rating=5.7,10&sort=num_votes,desc'

#opening url
test_url = urllib2.urlopen(url)
readHtml = test_url.read() #reading url
test_url.close() #close reading

bs = BeautifulSoup(readHtml,"lxml") #put the read website into BeautifulSoup

#iterate through the list of movies data thats within a specific div tag with a certain class
for movie in bs.find_all('div','lister-item mode-advanced'):
    title = movie.find_all('a',limit=2) #grab the first two a tags in all the movies data
    for name in title: #for each a tag grab the second a tag that contains movie name
        name.get_text()
    newName = name.get_text() #grabbing movie name from second a tag
    genres = movie.find('span','genre').contents[0] #find the genres from the span tag with class genre, will grab the first line of words (array)
    runtime = movie.find('span', 'runtime').contents[0]
    rating = movie.find('span', 'value').contents[0]
    year = movie.find('span','lister-item-year text-muted unbold').contents[0]
    print newName,year + ":", genres, "Run time:"+runtime, "\tRating:"+rating,"\n" #printing information scraped