from task_1 import r
import json
import pprint 



def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        # name=i
        year=i['year']
        for  x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("task_2.json","w")as file:
        json.dump(movie_dict,file,indent=4)
    return movie_dict
movie_list=group_by_year(r)



































































































# def group_by_year(r):
    
#     main_list={}
#     for i in r:
#         main_list[i["year"]]=i
#     return main_list
# z=group_by_year(r)
# pprint.pprint(z)

# with open("task_2.json","w")as file:
#     k=json.dump(z,file,indent=4)
        


# print(r)
#     main_list={}
#     for i in r:
#         main_list[i["year"]]=i
#     # pprint.pprint(main_list)
#     with open("task_2.json","w")as file:
#         json.dump(main_list,file,indent=4)

# with open("task_2.json","r") as file:
#     t=json.load(file)
# group_by_year(r)








































