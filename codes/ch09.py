#1、了解赞助额度最高的职业，所赞助的候选人
#2、对各党派总出资额最高的职业
#3、对出资额分组
#4、根据州统计赞助信息

########################################################

import numpy as np
import pandas as pd

fec = pd.read_csv('pydata-book-master\ch09\P00000001-ALL.csv')

##1、了解赞助额度最高的职业，所赞助的候选人
#定义党派
parties = {'Bachmann, Michelle':'Republican',
'Romney, Mitt':'Republican',
'Obama, Barack':'Democrat',
"Roemer, Charles E. 'Buddy' III" :'Republican',
'Pawlenty, Timothy':'Republican',
'Johnson, Gary Earl':'Republican', 
'Paul, Ron':'Republican', 
'Santorum, Rick':'Republican',
'Cain, Herman':'Republican',
'Gingrich, Newt':'Republican',
'McCotter, Thaddeus G':'Republican',
'Huntsman, Jon':'Republican',
'Perry, Rick':'Republican'}

#fec增加“党派”列，并关联候选人党派
fec['party'] = fec.cand_nm.map(parties)
fec['party'].value_counts()

#筛选出捐献额大于0的数据
fec = fec[fec.contb_receipt_amt>0]

#捐赠者职位清洗
occ_mapping = {
'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
'INFORMATION REQUESTED' : 'NOT PROVIDED',
'INFORMATION REQUESTED(BEST EFFORTS)':'NOT PROVIDED',
'C.E.O.' :'CEO'
}
f = lambda x: occ_mapping.get(x,x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

#
emp_mapping = {
'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
'INFORMATION REQUESTED':'NOT PROVIDED',
'SELF':'SELF-EMPLOYED',
'SELF EMPLOYED':'SELF-EMPLOYED',}
f = lambda x: emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f)
by_occupation = fec.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')

#筛选出捐赠额度大于200万美金的数据 
over_2mm = by_occupation[by_occupation.sum(1)>2000000]
over_2mm.plot(kind = 'barh')

########################################################
##2、对各党派总出资额最高的职业
def get_top_amounts(group,key,n=5):
	totals = group.groupby(key)['contb_receipt_amt'].sum()
	#根据key对totals进行降序排列
	return totals.order(ascending=False)[n:]

grouped = fec_mrbo.groupby('cand_nm')
grouped.apply(get_top_amounts,'contbr_occupation',n=7)
grouped.apply(get_top_amounts,'contbr_employer',n=10)

########################################################
#3、对出资额分组
#利用cut函数根据出资额的大小将数据离散化到多个面元中。
fec_mrbo = fec[fec.cand_nm.isin(['Obama,Barack','Romney,Mitt'])]
bins = np.array([0,10,100,1000,10000,100000,1000000,10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt,bins)

grouped = fec_mrbo.groupby(['cand_nm',labels])
#grouped.size().unstack(0)

bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)

normed_sums = bucket_sums.div(bucket_sums.sum(axis=1),axis=0)

normed_sums[:-2].plot(kind='barh',stacked=True)

########################################################
#4、根据州统计赞助信息
