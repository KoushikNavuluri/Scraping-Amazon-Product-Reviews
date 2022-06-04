# Scraping-Amazon-Product-Reviews-
Web Scraping Product Reviews from Amazon

### What Is Project About...???
Web Scraping the Top Reviews of desired products from Amazon ,Extracting the required data and saving it to a CSV file.


## STEPS :
```
1. Import Required Packages.
2. Provide Your Own Target Url.
3. Provide Your Headers And Replace Your Url In Referer.
4. Pass The Response For The Url.
5. Scrape The Response To Get The Source (HTML) Of The Website.
6. Choose Your Desired Parser , In This Case I Used LXML Parser.
7. Scrape The Required Data.
8. Remove If Any Extras, Using Strip or Replace Methods.
9. Create A Pandas DataFrame Using The Data.
10. Save It To CSV File.
```
Required Libraries:
==========================
```
pip install BeautifulSoup
pip install Pandas
pip install requests
```

## FAQ

#### What is the use of headers in the program ?

Some Modern Website are more safe and secure. The server tries to not allow the scrapers or robots to view their website. For this Purpose , we are using this headers parameters to safely authorize the website and visit the response.

#### What is the difference between 'lxml' and "html.parser" ?

1.html.parser - BeautifulSoup(markup, "html.parser")

   Advantages: Batteries included, Decent speed, Lenient (as of Python 2.7.3 and 3.2.)

   Disadvantages: Not very lenient (before Python 2.7.3 or 3.2.2)

2.lxml - BeautifulSoup(markup, "lxml")

   Advantages: Very fast, Lenient

   Disadvantages: External C dependency



## License

[MIT](https://choosealicense.com/licenses/mit/)
