# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

temp=pd.read_csv('data/user1_data.txt')
rowSum=temp.iloc[:,0].size
#print ('maxValueDict完成')
temp['type']=1
for i in range(1094785598,1112486201,17700):
    begin=i
    end=i+17700
    result=0
    count=0
    for i in range(1,rowSum):
        user_id=temp.loc[i]['userId']
        rating=int(temp.loc[i]['rating'])
        time=int(temp.loc[i]['timestamp'])
        if np.logical_and(time>begin,time<end):
            result+=rating
            count+=1
    if count!=0:
        print ('count=',count)
        print ('sum=',result)
        print ('average=',result/count)
        
