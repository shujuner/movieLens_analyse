# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
temp=pd.read_csv('result/fullData.csv')
#rnames = ['user_id', 'item_id', 'rating', 'time','count']
#mnames = ['user_id','item_id','rating','time', 'type0','type1','type2','type3','type4','type5','type6','type7','type8','type9','type10','type11','type12','type13','type14','type15','type16','type17','type18']
#
#ratings = pd.read_table(rpath,sep=',',header=None,names=rnames)
#print ('ratings读取完成')
#movies = pd.read_table(mpath,sep=',',header=None,names=mnames)
#print ('movies读取完成')
#rating_type=pd.merge(ratings,movies,how='left',on=['user_id','item_id'])
#
#rating_type.to_csv('result/data.csv')
#print ('合并完成')
#for ty in ['type1']:
#    findCount={} #用户id和自己所有评价的时间戳字典
#    userData=temp.groupby(['user_id']).apply(lambda x:x[ty][x['time_y']<101]).reset_index()
#    print (userData)
    
#    for user_id,max_time in zip(userData['user_id'],userData['time']):
#        findCount[user_id]=max_time
#    #length=len(data)
#    #print (length-data.index(100)-1)
#    rowSum=temp.iloc[:,0].size
#    for i in range(0,rowSum):
#        user_id=temp.loc[i]['user_id']
#        time=temp.loc[i]['time']
#        data=findCount[user_id]
#        length=len(data)
#        temp.loc[i][ty]=length-data.index(time)-1
#    temp.to_csv('result/Count_type.csv')
print (temp.columns)
#maxValueDict={}
#count=temp.groupby(['user_id','type1']).apply(lambda x:x['time'].values.max()).reset_index(name='max_time')
#for user_id,max_time in zip(count['user_id'],count['max_time']):
#    maxValueDict[user_id]=max_time
rowSum=temp.iloc[:,0].size
#print ('maxValueDict完成')
temp['type']=1
for i in range(1,rowSum):
    count=0
    user_id=temp.loc[i]['user_id']    
    time=temp.loc[i]['time']
    data=temp[np.logical_and(np.logical_and(temp['user_id']==user_id , temp['type1']==1),temp['time']>time)]
    length=data.iloc[:,0].size
    temp.loc[i]['type']=length
    print ('%.2f'%(i/rowSum))
temp.to_csv('result/testType.csv')