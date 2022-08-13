from django.contrib import admin
from digital_payment_index.models import historic_index_data,daily_index_data

admin.site.register(historic_index_data)
admin.site.register(daily_index_data)
# admin.site.register(Author)
# admin.site.register(Book)