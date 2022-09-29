import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_payment_index.settings')

import django
django.setup()

import csv
from digital_payment_index.models import  daily_index_data



# with open('digital_payment_index/digital_index_past_value.csv') as csvfile:
#       reader = csv.DictReader(csvfile)
#       for row in reader:
#             p = historic_index_data(date=row['\ufeffMonth'],index_value=row['Digital_Payment_Index'])
#             p.save()



with open('/app/digital_payment_index/DPI_Daily_Movement.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
             p =  daily_index_data(date=row['\ufeffDate'], UPI_Vol=row['UPI_VOL'], UPI_Val=row['UPI_VAL'],IMPS_Vol=row['IMPS_VOL'],IMPS_Val=row['IMPS_VAL'], NACH_Vol= row['NACH_VOL'] , NACH_Val=row['NACH_VAL'] ,NETC_Vol=row['NETC_VOL'],NETC_Val=row['NETC_VAL'],NEFT_Vol=row['NEFT_VOL'],NEFT_Val=row['NEFT_VAL'],RTGS_Vol=row['RTGS_VOL'],RTGS_Val=row['RTGS_VAL'],index_value=row['DPI'])
             p.save()
