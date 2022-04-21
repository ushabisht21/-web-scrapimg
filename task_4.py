from bs4 import BeautifulSoup
import requests
import json
import pprint
from task_1 import r
a=[]
def scrape_movie_details(link):
    b={}
    url=requests.get(link)
    soup=BeautifulSoup(url.text,"html.parser")
    title=soup.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
    # print(title)
    title1=title.find("div",class_="thumbnail-scoreboard-wrap")
    name=title1.find("h1",class_="scoreboard__title").get_text()
    b["title"]=name
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    b["Bio"]=movie_bio
 
    x=soup.find('ul',class_="content-meta info")

    y=x.find_all('li',class_="meta-row clearfix")
    # print(y)
    for i in y:
       b[i.find('div',class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())
    a.append(b)
    # return a
    # pprint.pprint(scrape_movie_details(link))
    with open("movie_details_task_4.json","w") as file:
            json.dump(a,file,indent=4)
    return a
url=r[0]["movie_url"]
scrape_movie_details(url)



