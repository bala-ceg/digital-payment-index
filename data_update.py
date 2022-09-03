import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_payment_index.settings')

import django
django.setup()

import pandas as pd
import requests
import datetime
import calendar
import time 
from digital_payment_index.models import daily_index_data
import numpy as np

theurl ='https://rbidocs.rbi.org.in/rdocs/content/docs/PSDDP04062020.xlsx'
n1=12

print("Enter index:")
index = int(input())


mydate = datetime.datetime.now()    
count = calendar.monthrange(mydate.year, mydate.month)[1]
month = mydate.strftime("%B") 
year = mydate.strftime("%Y")
month_year=str(month)+' '+ str(year)
			#print(month_year)

r=requests.get(theurl)
output = open('test.xls', 'wb')
output.write(r.content)
output.close()


xls = pd.ExcelFile('test.xls')
df1 = pd.read_excel(xls, month_year)
df1.drop(df1.tail(n1).index,inplace=True)
df1 = df1.reset_index()
col_list= list(df1.columns)
len1=df1.shape[0]
old_date = df1.iloc[len1-index]['Data for the day']
date = old_date.strftime("%d")

tmp = daily_index_data.objects.values().last()

if int(date) == 1 :
        UPI_Vol     = df1.iloc[len1-index]['Unnamed: 7'] 
        UPI_Val     = df1.iloc[len1-index]['Unnamed: 8'] 
        IMPS_Vol    = df1.iloc[len1-index]['Unnamed: 9'] 
        IMPS_Val    = df1.iloc[len1-index]['Unnamed: 10'] 
        NACH_Vol    = df1.iloc[len1-index]['Unnamed: 11'] + df1.iloc[len1-index]['Unnamed: 13'] 
        NACH_Val    = df1.iloc[len1-index]['Unnamed: 12'] + df1.iloc[len1-index]['Unnamed: 14'] 
        NETC_Vol    = df1.iloc[len1-index]['Unnamed: 15'] 
        NETC_Val    = df1.iloc[len1-index]['Unnamed: 16'] 
        NEFT_Vol    = df1.iloc[len1-index]['Unnamed: 3'] 
        NEFT_Val    = df1.iloc[len1-index]['Unnamed: 4'] 
        RTGS_Vol    = df1.iloc[len1-index][col_list[2]] 
        RTGS_Val    = df1.iloc[len1-index]['Unnamed: 2'] 
else:
        UPI_Vol     = df1.iloc[len1-index]['Unnamed: 7'] + tmp['UPI_Vol']
        UPI_Val     = df1.iloc[len1-index]['Unnamed: 8'] + tmp['UPI_Val']
        IMPS_Vol    = df1.iloc[len1-index]['Unnamed: 9'] + tmp['IMPS_Vol']
        IMPS_Val    = df1.iloc[len1-index]['Unnamed: 10'] + tmp['IMPS_Val']
        NACH_Vol    = df1.iloc[len1-index]['Unnamed: 11'] + df1.iloc[len1-index]['Unnamed: 13'] + tmp['NACH_Vol']
        NACH_Val    = df1.iloc[len1-index]['Unnamed: 12'] + df1.iloc[len1-index]['Unnamed: 14'] + tmp['NACH_Val']
        NETC_Vol    = df1.iloc[len1-index]['Unnamed: 15'] + tmp['NETC_Vol']
        NETC_Val    = df1.iloc[len1-index]['Unnamed: 16'] + tmp['NETC_Val']
        NEFT_Vol    = df1.iloc[len1-index]['Unnamed: 3'] +  tmp['NEFT_Vol']
        NEFT_Val    = df1.iloc[len1-index]['Unnamed: 4'] +  tmp['NEFT_Val']
        RTGS_Vol    = df1.iloc[len1-index][col_list[2]] + tmp['RTGS_Vol']
        RTGS_Val    = df1.iloc[len1-index]['Unnamed: 2'] + tmp['RTGS_Val']
        

UPI_Vol_0     = 20.30
UPI_Val_0     = 709.78
IMPS_Vol_0    = 528.60
IMPS_Val_0    = 43200.70
NETC_Vol_0    = 31.90
NETC_Val_0    = 88.12
NACH_Vol_0    = 2080.54
NACH_Val_0    = 69924.23
NEFT_Vol_0    = 1663.07
NEFT_Val_0    = 1153763.31
RTGS_Vol_0    = 88.40
RTGS_Val_0    = 8409647.78 


p0q0 = 2830565816 
p1q1= UPI_Vol*UPI_Val +IMPS_Vol*IMPS_Val + NETC_Vol*NETC_Val + NACH_Vol*NACH_Val + NEFT_Vol*NEFT_Val + RTGS_Vol*RTGS_Val
p0q1 = UPI_Val_0 * UPI_Vol + IMPS_Val_0 * IMPS_Vol + NETC_Val_0 * NETC_Vol + NACH_Val_0 * NACH_Vol + NEFT_Val_0 * NEFT_Vol + RTGS_Val_0 * RTGS_Vol
p1q0 = UPI_Val * UPI_Vol_0 + IMPS_Val * IMPS_Vol_0 + NETC_Val * NETC_Vol_0 + NACH_Val * NACH_Vol_0 + NEFT_Val * NEFT_Vol_0 + RTGS_Val * RTGS_Vol_0


fisher_coeff = (np.sqrt((p1q0/p0q0) * (p1q1/p0q1))) * 100 

#print(old_date)
if int(date) > 3 :
	op = (fisher_coeff * count) / (int(date))
else:
	op = fisher_coeff * ((-10.719 * np.log(int(date)))+ 21.8)



print("fisher_coeffient:",op)
daily_index_data.objects.create(date=old_date,UPI_Vol=UPI_Vol,UPI_Val=UPI_Val,IMPS_Vol=IMPS_Vol,IMPS_Val=IMPS_Val,NACH_Vol=NACH_Vol,NACH_Val=NACH_Val,NETC_Vol=NETC_Vol,NETC_Val=NETC_Val,NEFT_Vol=NEFT_Vol,NEFT_Val=NEFT_Val,RTGS_Vol=RTGS_Vol,RTGS_Val=RTGS_Val,index_value=op)
