import urllib2
from bs4 import BeautifulSoup

# Change this URL to scrape you website! This lets Beautiful Soup know
# what website your want to scrape
quote_page = ‘Enter your URL here.‘ # Enter your URL on this line
page = urllib2.urlopen(quote_page)

# This extracts the html from the website
soup = BeautifulSoup(page, 'html.parser')

# Update the class here to find your data. This searches the html parsed above
# and finds the data associated with the class you specify
number_box = soup.findAll(attrs={'class':['given-name','family-name','tel']}) # Change the parameters on this line to find your desired content.

# Loops through the found data and prints it out
for product in number_box:
        number = product.text.strip()
        print number
