import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.productionhub.com/casting-notices.aspx')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the listings div
casting_calls_list = soup.find(class_='listings')

# Pull text from all instances of media-body within listings div
casting_calls_list_items = casting_calls_list.find_all(class_='media-body')

# Create for loop to print out all casting calls 
for casting_call in casting_calls_list_items:
    f = open("casting-calls.html", "a")
    f.write(casting_call.prettify())
f.close()
print('Saved to %s' % f)
