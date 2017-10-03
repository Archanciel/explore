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
DATE_TIME_FORMAT_NO_YEAR = "%m/%d %H:%M:%S"
DATE_TIME_FORMAT_TZ = DATE_TIME_FORMAT + ' %Z%z'
DATE_TIME_FORMAT_TZ_NO_YEAR = DATE_TIME_FORMAT_NO_YEAR + ' %Z%z'
LA_TIMEZONE = 'US/Pacific'
NY_TIMEZONE = 'US/Eastern'
ZH_TIMEZONE = 'Europe/Zurich'
IN_TIMEZONE = 'Asia/Calcutta'
UTC_TIMEZONE = 'UTC'
MONTH = '09'
WINTER_MONTH = '11'
TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 3600
WINTER_TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 0

def printDate(location, datetimeObj):
    printDateNoDst(location, datetimeObj)
    print('     tm_isdst=' + str(datetimeObj.timetuple()[8]))

def printDateNoDst(location, datetimeObj):
    if len(location) == 3:
        print(location + ': ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))
    else:
        print(location + ':  ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))

def printAndStoreOrderDateUtcTS(investor, datetimeObj, orderDic):
    print(investor + ':  ' + datetimeObj.strftime(DATE_TIME_FORMAT_TZ))
    datetimeObjUTC = datetimeObj.astimezone(timezone(UTC_TIMEZONE))
    timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
    timeStampStr = str(int(timeStampUTC))
    print('     UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
    print('     TS:  ' + timeStampStr)
    orderDic[investor] = timeStampStr
    
def printLag(icoDatetimeObjLA, orderDatetimeObj):
    utcLagLA = float(icoDatetimeObjLA.strftime('%z')) / 100
    utcLagOrderDate = float(orderDatetimeObj.strftime('%z')) / 100
    
    if ((utcLagLA < 0) and (utcLagOrderDate < 0)) or ((utcLagLA > 0) and (utcLagOrderDate > 0)):
        totalLag = abs(abs(utcLagLA) - abs(utcLagOrderDate))
    else:
        totalLag = abs(abs(utcLagLA) + abs(utcLagOrderDate))
    
    print("     LAG: %.1f" % totalLag)    

def browseOrders(orderDic, viewerTimezone, dst):
    print('--Orders {}--'.format(viewerTimezone))
    for key, value in orderDic.items():
        localDateStr = timestamp2localdate(value, viewerTimezone, dst)
        #print('dst-->{}'.format(dst))
        print("{} {} {} d-{}".format(key, value, localDateStr, dst))
    print('')   

def timestamp2localdate(strTimestamp, localTimeZone, dst):
    # function converts a UTC timestamp into timezone Gregorian date
    intTimeStamp = int(strTimestamp)
    tsCorr = 3600 * dst
    intTimeStamp -= tsCorr
    datetimeUTC = datetime.fromtimestamp(intTimeStamp).replace(tzinfo=timezone('UTC'))
    datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
    datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
    datetimeLocal = datetimeUTC.astimezone(timezone(localTimeZone))
    print('tsCorr: {} dst-->{}'.format(tsCorr,dst))
    return datetimeLocal.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR)

print("-- Summer ICO start date/time --")
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

print("\n-- Winter ICO start date/time --")
icoLocDateStr = '2017/' + WINTER_MONTH + '/30 09:00:00'
icoDatetimeObjUnlocalized = datetime.strptime(icoLocDateStr, DATE_TIME_FORMAT)
icoDatetimeObjLA_Winter = timezone(LA_TIMEZONE).localize(icoDatetimeObjUnlocalized)
printDate('LA', icoDatetimeObjLA_Winter)

icoDatetimeObjNY = icoDatetimeObjLA_Winter.astimezone(timezone(NY_TIMEZONE))
printDate('NY', icoDatetimeObjNY)

icoDatetimeObjZH = icoDatetimeObjLA_Winter.astimezone(timezone(ZH_TIMEZONE))
printDate('ZH', icoDatetimeObjZH)

icoDatetimeObjIN = icoDatetimeObjLA_Winter.astimezone(timezone(IN_TIMEZONE))
printDate('IN', icoDatetimeObjIN)

icoDatetimeObjUTC = icoDatetimeObjLA_Winter.astimezone(timezone(UTC_TIMEZONE))
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Placing summer orders --")
printDateNoDst('LA', icoDatetimeObjLA)
orderDic = {}
normanOrderDateStr = '2017/' + MONTH + '/30 12:01:55'
orderDatetimeObjUnlocalized = datetime.strptime(normanOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(NY_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('NO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA, orderDatetimeObj)

zoeOrderDateStr = '2017/' + MONTH + '/30 18:01:57'
orderDatetimeObjUnlocalized = datetime.strptime(zoeOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(ZH_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('ZO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA, orderDatetimeObj)

indiraOrderDateStr = '2017/' + MONTH + '/30 21:32:07'
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('IN', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA, orderDatetimeObj)

print("\n-- Browsing summer orders --")
browseOrders(orderDic, LA_TIMEZONE, 1)
browseOrders(orderDic, NY_TIMEZONE, 1)
browseOrders(orderDic, IN_TIMEZONE, 0)
browseOrders(orderDic, ZH_TIMEZONE, 1)

print("\n-- Placing winter orders --")
printDateNoDst('LA', icoDatetimeObjLA_Winter)
orderDic = {}
normanOrderDateStr = '2017/' + WINTER_MONTH + '/30 12:01:55'
orderDatetimeObjUnlocalized = datetime.strptime(normanOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(NY_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('NO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_Winter, orderDatetimeObj)

zoeOrderDateStr = '2017/' + WINTER_MONTH + '/30 18:01:57'
orderDatetimeObjUnlocalized = datetime.strptime(zoeOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(ZH_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('ZO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_Winter, orderDatetimeObj)

indiraOrderDateStr = '2017/' + WINTER_MONTH + '/30 22:32:07' #note that India winter hour differs from summer hour !
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObj = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
printAndStoreOrderDateUtcTS('IN', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_Winter, orderDatetimeObj)

print("\n-- Browsing winter orders --")
browseOrders(orderDic, LA_TIMEZONE, 0)
browseOrders(orderDic, NY_TIMEZONE, 0)
browseOrders(orderDic, IN_TIMEZONE, 0)
browseOrders(orderDic, ZH_TIMEZONE, 0)