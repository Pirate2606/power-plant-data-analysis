import pandas as pd
from datetime import timedelta
from datetime import datetime


def previous_day_yield(plant_data):
    last_date = list(plant_data.tail(1)['DATE_TIME'])[0].split('-')
    date = last_date[0]
    month = last_date[1]
    year = last_date[2].split(" ")[0]

    previous_date = datetime(int(year), int(month), int(date)) - timedelta(days=1)
    previous_date_str = previous_date.strftime("%d-%m-%Y") + " 00:00"

    i = 0
    ans = 0.0
    for data in plant_data['DATE_TIME']:
        i += 1
        if previous_date_str == data:
            j = i - 1
            for x in plant_data.iloc[i:]['DAILY_YIELD']:
                if previous_date_str[:11] not in plant_data.iloc[j]['DATE_TIME']:
                    break
                j += 1
                ans += float(x)
            break
    return ans

def total_yield_given_day(plant_data, year, month, date):

    dateTime = datetime(int(year), int(month), int(date))
    the_day = dateTime.strftime("%d-%m-%Y") + " 00:00"

    i = 0
    ans = 0.0
    for data in plant_data['DATE_TIME']:
        i += 1
        if the_day == data:
            j = i - 1
            for x in plant_data.iloc[i:]['TOTAL_YIELD']:
                if the_day[:11] not in plant_data.iloc[j]['DATE_TIME']:
                    break
                j += 1
                ans += float(x)
            break
    return ans

def mean_difference(plant_data):
    last_date = list(plant_data.tail(1)['DATE_TIME'])[0].split('-')
    date = last_date[0]
    month = last_date[1]
    year = last_date[2].split(" ")[0]
    ac = 0.0
    dc = 0.0

    previous_date = datetime(int(year), int(month), int(date)) - timedelta(days=1)
    while previous_date.weekday() != 6:
        previous_date -= timedelta(days=1)
    start_date = previous_date - timedelta(days=6)
    end_date = (previous_date + timedelta(days=1)).strftime("%d-%m-%Y") + " 00:00"
    ac, dc = get_AC(plant_data, start_date, end_date)
    return ((ac / 7) - (dc / 7))
    

def get_AC(plant_data, start_date, end_date):
    start = start_date.strftime("%d-%m-%Y") + " 00:00"
    i = 0
    ac = 0.0
    dc = 0.0
    for data in plant_data['DATE_TIME']:
        i += 1
        if start == data:
            j = i - 1
            for (x, y) in zip(plant_data.iloc[i:]['AC_POWER'], plant_data.iloc[i:]['DC_POWER']):
                if end_date[:11] in plant_data.iloc[j]['DATE_TIME']:
                    break
                j += 1
                ac += float(x)
                dc += float(y)
            break
    return (ac, dc)
