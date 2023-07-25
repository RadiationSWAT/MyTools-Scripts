import newspaper
import os
from requests_html import HTMLSession

# ---------------------------------------sports--------------------------------------------------------
session = HTMLSession()
# URL link for the sports category
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
r = session.get(url)
# this line is utilised to scroll the google news category page to gather the articles up to the specified limit.
r.html.render(sleep=1, scrolldown=6)

articles = r.html.find('article')
newsLinks = []

for i in articles:
    try:
        newsitem = i.find('a', first=True)
        rawLink = newsitem.attrs['href']
        # URL is obtained by looking at the inspect element of the web page and extracting the link that is stored in html 'a' class
        # All articles within the link contains the starting link as mentioned as a string in fullLink variable.
        fullLink = str("https://news.google.com" + rawLink[1:-1])
        newsLinks.append(fullLink)
    except:
        pass

print(len(newsLinks))
print(newsLinks[5:10])



item = 1

switch = 0
# 100 articles are stored in the directory mentioned below.
os.chdir("Python_classifier\Sports\Training")
for url in newsLinks:
    if item <= 100 and switch == 0:
        try:
            file2write = open("TrSportsArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()
            text = url_i.text
            if(len(text) > 0):
                file2write.write(text)
                print(url_i)
                item = item + 1
                file2write.close()
            if(item == 101):
                # storing another 100 in the testing subfolder
                os.chdir("..\Testing")
                switch = 1
        except:
            pass

    elif item > 100 and switch == 1:
        try:
            file2write = open("TeSportsArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()
            text = url_i.text
            if(len(text) > 0):
                file2write.write(text)
                print(url_i)
                item = item + 1
                file2write.close()
        except:
            pass
    elif item >= 200:
        break

# -------------------------------------------------technology---------------------------------------------------------------------------
# same logic for technology
session = HTMLSession()
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
r = session.get(url)

r.html.render(sleep=1, scrolldown=6)

articles = r.html.find('article')
newsLinks = []

for i in articles:
    try:
        newsitem = i.find('a', first=True)
        rawLink = newsitem.attrs['href']
        fullLink = str("https://news.google.com" + rawLink[1:-1])
        newsLinks.append(fullLink)
    except:
        pass

print(len(newsLinks))
print(newsLinks[5:10])

item = 1

switch = 0

os.chdir("Python_classifier\Technology\Training")
for url in newsLinks:
    if item <= 100 and switch == 0:
        try:
            file2write = open("TrTechnologyArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()
            text = url_i.text
            if(len(text) > 0):
                file2write.write(text)
                item = item + 1
                file2write.close()
            if(item == 101):
                os.chdir("..\Testing")
                switch = 1
        except:
            pass

    elif item > 100 and switch == 1:
        try:
            file2write = open("TeTechnologyArticle" + str(item) + ".txt", 'w')
            url_i = newspaper.Article(url=(url), language='en')
            url_i.download()
            url_i.parse()
            text = url_i.text
            if(len(text) > 0):
                file2write.write(text)
                item = item + 1
                file2write.close()
        except:
            pass
    elif item >= 200:
        break