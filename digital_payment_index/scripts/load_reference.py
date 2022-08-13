import csv
from digital_payment_index.models import daily_data

with open('digital_payment_index/DPI_Daily_Movement.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
             p = daily_data(date=row['\ufeffDate'], UPI_Vol=row['UPI_VOL'], UPI_Val=row['UPI_VAL'],IMPS_Vol=row['IMPS_VOL'],IMPS_Val=row['IMPS_VAL'],NETC_Vol=['NETC_VOL'],NETC_Val=row['NETC_VAL'],NEFT_Vol=row['NEFT_VOL'],NEFT_Val=row['NEFT_VAL'],RTGS_Vol=row['RTGS_VOL'],RTGS_Val=row['RTGS_VAL'],index_value=row['DPI'])
             p.save()