from datetime import datetime
from pytz import timezone
import time

'''
Scenario
--------
	
Norman, in New York, Zoé in Zurich
and Indira in India are placing an
order on a Los Angeles ICO which 
starts on Sept (Nov) 30th, 2017 at 9.00
PDT time.

The 3 orders are stored with a UTC
time stamp in the ICO database.

They can be accessed by anybody
using their browser.
'''
DATE_TIME_FORMAT = "%Y/%m/%d %H:%M:%S"
DATE_TIME_FORMAT_TZ = DATE_TIME_FORMAT + ' %Z%z'
LA_TIMEZONE = 'US/Pacific'
NY_TIMEZONE = 'US/Eastern'
ZH_TIMEZONE = 'Europe/Zurich'
IN_TIMEZONE = 'Asia/Calcutta'
UTC_TIMEZONE = 'UTC'
MONTH = '09'
#MONTH = '11'
TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 3600
#TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 0

def printDate(location, datetimeObj):
    if len(location) == 3:
        print(location + ': ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))
    else:
        print(location + ':  ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))
    print('     tm_isdst=' + str(datetimeObj.timetuple()[8]))


def printAndStoreOrderDateUtcTS(investor, datetimeObj, orderDic):
    print(investor + ':  ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))
    datetimeObjUTC = datetimeObj.astimezone(timezone(UTC_TIMEZONE))
    timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
    timeStampStr = str(int(timeStampUTC))
    print('     UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
    print('     TS:  ' + timeStampStr)
    orderDic[investor] = timeStampStr


def browseOrders(orderDic, viewerTimezone):
    print('\n--Orders {}--'.format(viewerTimezone))
    for key, value in orderDic.items():
        localDateStr = timestamp2localdate(value, viewerTimezone)
        print("{} {} {}".format(key, value, localDateStr))
        

def timestamp2localdate(strTimestamp, localTimeZone):
    # function converts a UTC timestamp into timezone Gregorian date
    intTimeStamp = int(strTimestamp)
    intTimeStamp -= TIMESTAMP_TO_DATE_CORRECTION_FACTOR 
    datetimeUTC = datetime.fromtimestamp(intTimeStamp).replace(tzinfo=timezone('UTC'))
    datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
    datetimeUTC = timezone(LA_TIMEZONE).localize(datetimeUnlocalized)
    datetimeLocal = datetimeUTC.astimezone(timezone(localTimeZone))
    # dst = str(datetimeLocal.timetuple()[8])
    # print('dst-->{}'.format(dst))
    return datetimeLocal.strftime(DATE_TIME_FORMAT_TZ)

print("-- ICO start date/time --")
icoLocDateStr = '2017/' + MONTH + '/30 09:00:00'
icoDatetimeObjUnlocalized = datetime.strptime(icoLocDateStr, DATE_TIME_FORMAT)
icoDatetimeObjLA = timezone(LA_TIMEZONE).localize(icoDatetimeObjUnlocalized)
printDate('LA', icoDatetimeObjLA)

icoDatetimeObjNY = icoDatetimeObjLA.astimezone(timezone(NY_TIMEZONE))
printDate('NY', icoDatetimeObjNY)

icoDatetimeObjZH = icoDatetimeObjLA.astimezone(timezone(ZH_TIMEZONE))
printDate('ZH', icoDatetimeObjZH)

icoDatetimeObjIN = icoDatetimeObjLA.astimezone(timezone(IN_TIMEZONE))
printDate('IN', icoDatetimeObjIN)

icoDatetimeObjUTC = icoDatetimeObjLA.astimezone(timezone(UTC_TIMEZONE))
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Placing orders --")
orderDic = {}
normanOrderDateStr = '2017/' + MONTH + '/30 12:01:55'
orderDatetimeObjUnlocalized = datetime.strptime(normanOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(NY_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('NO', orderDatetimeObj, orderDic)

zoeOrderDateStr = '2017/' + MONTH + '/30 18:01:57'
orderDatetimeObjUnlocalized = datetime.strptime(zoeOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(ZH_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('ZO', orderDatetimeObj, orderDic)

indiraOrderDateStr = '2017/' + MONTH + '/30 21:32:07'
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('IN', orderDatetimeObj, orderDic)

browseOrders(orderDic, LA_TIMEZONE)
browseOrders(orderDic, NY_TIMEZONE)
browseOrders(orderDic, IN_TIMEZONE)
browseOrders(orderDic, ZH_TIMEZONE)