# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
temp = pd.read_csv('data/movieLens100k_1.txt')

#maxValueDict={}
#count=temp.groupby(['user_id']).apply(lambda x:x['time'].values.max()).reset_index(name='max_time')
#for user_id,max_time in zip(count['user_id'],count['max_time']):
#    maxValueDict[user_id]=max_time
#print(maxValueDict)
temp['count']=1 
findCount={} #用户id和自己所有评价的时间戳字典
userData=temp.groupby(['user_id']).apply(lambda x:sorted(x['time'])).reset_index(name='time')
for user_id,max_time in zip(userData['user_id'],userData['time']):
    findCount[user_id]=max_time
#length=len(data)
#print (length-data.index(100)-1)
rowSum=temp.iloc[:,0].size
for i in range(0,rowSum):
    user_id=temp.loc[i]['user_id']
    time=temp.loc[i]['time']
    data=findCount[user_id]
    length=len(data)
    temp.loc[i]['count']=length-data.index(time)-1
temp.to_csv('addMovieCount.csv')
    
    
