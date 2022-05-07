
import json
from task_5 import list1
def analyse_movies_language (movie_list):
    list1=[]
    lang_list={}
    for i in movie_list:
        if i["Director:"] not in list1:
            list1.append(i["Director:"])
    for i in list1:
            key=i
            # print(key)
            count=0
            for j in movie_list:
                lang=j["Director:"]
                if str(i)==str(lang):
                    count=count+1
            lang_list.update(({key:count}))
    with open("Director.json","w") as f:
        json.dump(lang_list,f,indent=6)
    return lang_list

            # print(list1)
analyse_movies_language(list1)

 























