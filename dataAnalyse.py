# -*- coding: utf-8 -*-

#user_item=pd.read_csv('data/user_item.txt')
#movie = pd.read_csv('data/movie.csv')
#temp=pd.merge(user_item,movie,how='left',on='item_id')
import pandas as pd
import numpy as np
#rpath = 'data/ratings.txt'
#mpath = 'data/movies.txt'
#
#rnames = ['user_id', 'item_id', 'rating', 'time']
#mnames = ['item_id', 'title', 'type']
#
#ratings = pd.read_table(rpath,sep=',',header=None,names=rnames)
#print ('ratings读取完成')
#movies = pd.read_table(mpath,sep=',',header=None,names=mnames)
#print (movies[:])
#print ('movies读取完成')
#rating_type=pd.merge(ratings,movies,how='left',on='item_id')
#print ('合并完成')
#rating_type.to_csv('result/rating_Type.csv')
#data = pd.read_csv('result/rating_Type.csv')
#for i in range(3):
#    data['type_%d'%(i)] = data['type'].apply(
#            lambda x:x.split("|")[i] if len(x.split(";")) > i else " "
#        )
#del data['type']
#data.to_csv('user2.csv')

temp = pd.read_csv('data/ratings.txt')

maxValueDict={}
count=temp.groupby(['user_id']).apply(lambda x:x['time'].values.max()).reset_index(name='max_time')
for user_id,max_time in zip(count['user_id'],count['max_time']):
    maxValueDict[user_id]=max_time
#print(maxValueDict)
temp['count']=1
findCount={}
userData=temp.groupby(['user_id']).apply(lambda x:sorted(x['time'])).reset_index(name='time')
for user_id,max_time in zip(userData['user_id'],userData['time']):
    findCount[user_id]=max_time
print (findCount[1].index(1))










#rowSum=temp.iloc[:,0].size
#for i in range(0,rowSum):
#    if temp.loc[0]['time']
#temp['max']=1
#temp.loc[0]['max']=0
#print (temp.loc[0].values)
#res=pd.DataFrame()
#count=temp.groupby(['user_id']).apply(lambda x: x['item_id'][np.logical_and(x['time']<later,x['time']> before).values].count()).reset_index(name='item_count')
#count1=temp.groupby(['user_id']).apply(lambda x: x['rating'][np.logical_and(x['time']<later,x['time']> before).values].sum()).reset_index(name='rating_sum')
#count['rating_sum']=count1['rating_sum']
#count['average']=count['rating_sum']/count['item_count']
#res=res.append(count,ignore_index=True)
#res.to_csv('%s.csv' % ('uesr'), index=False)















