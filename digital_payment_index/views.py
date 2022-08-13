from django.shortcuts import render
import pandas as pd
import requests
import datetime
import calendar
import time 
import random
from digital_payment_index.models import historic_index_data,daily_index_data
import numpy as np



def home(request):
        
        
    item1 =  historic_index_data.objects.values()
    df1 = pd.DataFrame(item1)
    df1 = df1.drop(['id'], axis=1)

    item2 =  daily_index_data.objects.values()
    df2 = pd.DataFrame(item2)
    df2 = df2.drop(['id'], axis=1)
    
    xdata1 = df1['date'].tolist()
    xdata1 = [(int(time.mktime(item.timetuple()))) * 1000 for item in xdata1]
    #print(xdata)
    ydata1 = df1['index_value'].tolist()
   
    xdata2 = df2['date'].tolist()
    xdata2 = [(int(time.mktime(item.timetuple()))) * 1000 for item in xdata2]
    #print(xdata)
    ydata2 = df2['index_value'].tolist()


    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
  


    chartdata1 = {'x': xdata1,
        'name1': 'DPI value', 'y1': ydata1, 'extra1': extra_serie1, 'kwargs1': { 'color': '#a4c639' },
        
    }

   
   
    # print (chartdata1)
    # print (chartdata2)



    charttype1 = "lineChart"
    chartcontainer1 = 'linechart_container1'  # container name
     
    data = {
        'charttype1': charttype1,
        'chartdata1': chartdata1,
        'chartcontainer1': chartcontainer1,
        'extra1': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }

    }


    return render(None,'home.html',data)

def dailydpi(request):


    item1 =  daily_index_data.objects.values()
    df1 = pd.DataFrame(item1)
    df1 = df1.drop(['id'], axis=1)
    
    xdata1 = df1['date'].tolist()
    xdata1 = [(int(time.mktime(item.timetuple()))) * 1000 for item in xdata1]
    #print(xdata)
    ydata1 = df1['index_value'].tolist()
   
    


    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
  


    chartdata2 = {'x': xdata1,
        'name1': 'DPI value', 'y1': ydata1, 'extra1': extra_serie2, 'kwargs1': { 'color': '#a4c639' },
        
    }



    charttype2 = "lineChart"
    chartcontainer2 = 'linechart_container2'  # container name
     
    data = {
        'charttype2': charttype2,
        'chartdata2': chartdata2,
        'chartcontainer2': chartcontainer2,
        'extra2': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }

    }


    return render(None,'dailydpi.html',data)

