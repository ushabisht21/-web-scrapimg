from task_2 import movie_list
from task_1 import scrap_top_list
import json
import pprint
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]  
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if int(x)<= dec10 and int(x)>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open("task_3.json","w")as file:
        json.dump(moviedec,file,indent=4)
    return(moviedec)
print(group_by_decade(movie_list))






























# year=[]
# def group_by_decade(t):
#     dict={}
#     for i in t.keys():
#         year.append(i)
#     year.sort()
#     # print(year)

#     j=0
    
#     decade_list=[]
#     while j<len(year):
#         year_1=(int(year[j])//10)*10
#         if year_1 not in decade_list:
#             decade_list.append(year_1)
#         j=j+1
#     # return (decade_list)
    
    
#     final=[]
#     for i in decade_list:
#         range=i+9
#         for k in t:
#             x=int(k)
#             if x>=i and int(x)<=range:
#                 for s in t[str(x)]:
#                    final.append(s)
#                 print(final) 

#        for k,v in t.items():
#            if int(k)>=i and int(k)<=range:
#             #    print(k)
#                 # final.append(t[int(k)])
#                 for s in t[k]:
# #                     print(s)
# #                     # final.append(s)
# #             # print(final)
                
#         dict[i]=final
# #     return dict
# # y=group_by_decade(t)
# # print(y)
# # pprint.pprint(group_by_decade())
#     with open("task3.json","w")as file:
#         json.dump(dict,file,indent=4)
#         return dict
# group_by_decade(t)
# # print(res)




































# with open("task3.json","w")as file:
#     x=json.dump(p,file,indent=4)
    
        


# from task_1 import r
# from task_2 import group_by_year
# import json

# dec_arg=r()
# new_arg=group_by_year(dec_arg)
# def group_by_decade(movies):
#     moviedec={}
#     list1=[]
#     for index in movies:
#         mod=index%10
#         decade=index-mod
#         if decade not in list1:
#             list1.append(decade)
#     # print(list1)
#     list1.sort()
#     # print(list1) 

#     for i in list1:
#         moviedec[i]=[]

#     print(moviedec)
#     for i in moviedec:
#         dec10 = i+9
#         for x in movies:
#             if x<=dec10 and x>=i:
#                 for v in movies[x]:
#                     moviedec[i].append(v)
#     with open("task_3.json","w")as f:
#         json.dump(moviedec,f,indent=4)
#     return (moviedec)
# print(group_by_decade(new_arg))
