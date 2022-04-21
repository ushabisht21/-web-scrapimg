# from distutils.filelist import findall
# from msilib.schema import tables
from bs4 import BeautifulSoup 
import requests
import pprint
import json


def scrap_top_list():
    main_list=[]
    url='https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies'
    data=requests.get(url)
    # print(data)
    x=data.text
    soup=BeautifulSoup(x,'html.parser')
    # print(soup)
    main_data=soup.find('table',class_='table')
    # print(main_data)
    x=main_data.find_all('tr')
    # print(x)
    # y=x.find('td')
    # print(y)
    
    for i in x[1:]:
        y=i.findAll("td")
        dic={}
        # year=dic[-1][1:5]
        # year1=int(year)
        # dic["year"]=" ".join(y[2].text[-6:-1].split())
        dic["position."]=" ".join(y[0].text.split())
        dic["rating"]=" ".join(y[1].text.split())
        dic["movie_name"]=" ".join(y[2].text.split())
        dic["year"]=" ".join(y[2].text[-6:-2].split())
        dic["review"]=" ".join(y[3].text.split())
        z=y[2].find("a")["href"]
        dic["movie_url"]='https://www.rottentomatoes.com'+z
    # return main_list
    # print(dic)
        main_list.append(dic)
    # pprint.pprint(main_list)

    with open("scrap_top_list_task_1.json","w") as f:
        json.dump(main_list,f,indent =2)

with open("scrap_top_list_task_1.json","r") as file:
    r=json.load(file)
    # pprint.pprint(r)


# print(r)
scrap_top_list()
