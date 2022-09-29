import csv
from digital_payment_index.models import  historic_index_data



with open('digital_payment_index/digital_index_past_value.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
            p = historic_index_data(date=row['\ufeffMonth'],index_value=row['Digital_Payment_Index'])
            p.save()
