# Import The Required Packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Provide Your Own Target Url
url = "https://www.amazon.in/dp/B09G9H3RZH/"

# Provide Your Headers And Replace Your Url In Referer
HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5',
      'referer':'https://www.amazon.in/dp/B09G9H3RZH/'})

# Pass The Response For The Url
allow = requests.get(url,headers=HEADERS)

# Scrape The Response To Get The Source (HTML) Of The Website.
# Choose Your Desired Parser , In This Case I Used LXML Parser.
soup = BeautifulSoup(allow.text,'lxml')

#To View The Nicer Version Of Your Source( HTML )
print(soup.prettify())

customers_data=[]

# Scrape The Customers Data
for i in soup.findAll('span',{'class':'a-profile-name'}):
    customers_data.append(i.text)

# Remove The Duplicates
customers = [] 
[customers.append(i) for i in customers_data if i not in customers]     


review_titles = []

# Scrape The Review Titles
for i in soup.findAll("a",{'class':'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'}): # the tag which is common for all the names of products
    review_titles.append(i.text.strip('\n'))
 
review_texts=[]

# Scrape The Review Texts / Comments
# Remove All The Extras Using Strip And Replace Methods
for i in soup.findAll("div",{'data-hook':"review-collapsed"}): # the tag which is common for all the names of products
    review_texts.append(i.text.strip('\n').replace('\n                \n\n\n\n\xa0','').replace('The media could not be loaded.','').lstrip(' '))
 

# Create A DataFrame Reviews Data
reviews_data = pd.DataFrame(customers,columns=["Customers"],index=range(1,len(reviews_data)+1))    
    
#Add Review Titles Column To The Data Frame 
reviews_data["Review Titles"] = review_titles

#Add Review Texts/Comments Column To The Data Frame
reviews_data["Review Texts/Comments"] = review_texts

#Save Your DataSet To CSV File ..........
reviews_data.to_csv("YOUR FILENAME.csv")
