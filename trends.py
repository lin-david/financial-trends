from pytrends.request import TrendReq
import json

class DateValuePair:
    def __init__(self, date, value):
        self.date = date;
        self.value = value;

    def getDate(self):
        return self.date

    def getValue(self):
        return self.value

    def __str__(self):
        return "{Date: "+str(self.getDate())+" | Value: "+str(self.getValue())+"}"


class Trends:

    pytrend = None
    path = ""

    def __init__(self, google_username, google_password):
        try:
            self.pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
        except:
            print("Error authenticating with Google account")

    def getTrendData(self, search_term, start_date, end_date):
        if self.pytrend == None:
            print("No Google account to authenticate with")
            return

        start_ints = start_date.split('/')
        end_ints = end_date.split('/')

        # check if invalid time window is given
        start_month_id = int(start_ints[1])*12 + int(start_ints[0])
        end_month_id = int(end_ints[1])*12 + int(end_ints[0])
        if start_month_id < 24136: # April 20111
            raise Exception("start month too early")
        if end_month_id > 24203: # November 2016
            raise Exception("end month too late")

        duration = end_month_id - start_month_id

        DVpairs = []

        trend_params = {'q': search_term, 'date': start_date + ' ' + str(duration) + 'm'}

        raw_output = self.pytrend.trend(trend_params, return_type='json')
        print(raw_output)
        unfiltered_rows = raw_output['table']['rows']


        for r in unfiltered_rows:
            date = r['c'][0]['v']
            value = r['c'][1]['v']
            if value != None:
                DVpairs.append(DateValuePair(date, value))

        return DVpairs
