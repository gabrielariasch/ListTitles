#GOAL: TITLE OF EVERY BOOK WITH 2 STAR RATING.

import bs4
import lxml #helps us process XML and HTML
from bs4 import BeautifulSoup
import requests

#Base URL
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

#Will run through the 50 pages.
for n in range(1,51):

    #Will scape through each page - n will update everytime
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    # Turns it into a soup
    soup = bs4.BeautifulSoup(res.text,'lxml')

    #Looks for product pods.
    books = soup.select('.product_pod')

    #For each of those books in product pod it will check if they are two star rated.
    for book in books:
        if 'star-rating Two' in str(books):
            #If true, grabs the title and appends it to the list
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
