from datetime import datetime
from pytz import timezone
import time
from datetimeutil import DateTimeUtil
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
DATE_TIME_FORMAT_ARROW = 'YYYY/MM/DD HH:mm:ss'
DATE_TIME_FORMAT_TZ_ARROW = DATE_TIME_FORMAT_ARROW + ' ZZ'
DATE_TIME_FORMAT_ARROW_NO_YEAR = 'MM/DD HH:mm:ss'
DATE_TIME_FORMAT_TZ_ARROW_NO_YEAR = 'MM/DD HH:mm:ss' + ' ZZ'
LA_TIMEZONE = 'US/Pacific'
NY_TIMEZONE = 'US/Eastern'
ZH_TIMEZONE = 'Europe/Zurich'
IN_TIMEZONE = 'Asia/Calcutta'
UTC_TIMEZONE = 'UTC'
SUMMER_MONTH = '09'
WINTER_MONTH = '11'
TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 3600
WINTER_TIMESTAMP_TO_DATE_CORRECTION_FACTOR = 0

def printDate(location, datetimeObj):
    if len(location) == 3:
        print(location + ': ' + datetimeObj.format(DATE_TIME_FORMAT_TZ_ARROW))
    else:
        print(location + ':  ' + datetimeObj.format(DATE_TIME_FORMAT_TZ_ARROW))

def printAndStoreOrderDateTS(investor, datetimeObj, orderDic):
    print(investor + ':  ' + datetimeObj.format(DATE_TIME_FORMAT_TZ_ARROW))
    timeStamp = datetimeObj.timestamp
    timeStampStr = str(int(timeStamp))
    print('     UTC: ' + DateTimeUtil.timeStampToArrowLocalDate(timeStamp, UTC_TIMEZONE).format(DATE_TIME_FORMAT_TZ_ARROW))
    print('     TS:  ' + timeStampStr)
    orderDic[investor] = timeStampStr
    
def printLag(icoDatetimeObjLA, orderDatetimeObj):
    utcLagLA = float(icoDatetimeObjLA.format('Z')) / 100
    utcLagOrderDate = float(orderDatetimeObj.format('Z')) / 100
    
    if ((utcLagLA < 0) and (utcLagOrderDate < 0)) or ((utcLagLA > 0) and (utcLagOrderDate > 0)):
        totalLag = abs(abs(utcLagLA) - abs(utcLagOrderDate))
    else:
        totalLag = abs(abs(utcLagLA) + abs(utcLagOrderDate))
    
    print("     LAG: %.1f" % totalLag)    

def browseOrders(orderDic, viewerTimezone):
    print('--Orders {}--'.format(viewerTimezone))
    for key, value in orderDic.items():
        localDateStr = timestamp2localdate(value, viewerTimezone)
        #print('dst-->{}'.format(dst))
        print("{} {} {}".format(key, value, localDateStr))
    print('')   

def timestamp2localdate(strTimestamp, localTimeZone):
    # function converts a UTC timestamp into timezone Gregorian date
    intTimeStamp = int(strTimestamp)
    datetimeLocal = DateTimeUtil.timeStampToArrowLocalDate(intTimeStamp, localTimeZone)
    return datetimeLocal.format(DATE_TIME_FORMAT_ARROW_NO_YEAR)

print("-- Summer ICO start date/time --")
icoLocDateStr = '2017/' + SUMMER_MONTH + '/30 09:00:00'
icoDatetimeObjLA_summer = DateTimeUtil.dateTimeStringToArrowLocalDate(icoLocDateStr, LA_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printDate('LA', icoDatetimeObjLA_summer)

icoDatetimeObjNY = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_summer, NY_TIMEZONE)
printDate('NY', icoDatetimeObjNY)

icoDatetimeObjZH = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_summer, ZH_TIMEZONE)
printDate('ZH', icoDatetimeObjZH)

icoDatetimeObjIN = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_summer, IN_TIMEZONE)
printDate('IN', icoDatetimeObjIN)

icoDatetimeObjUTC = icoDatetimeObjLA_summer.to(UTC_TIMEZONE)
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Winter ICO start date/time --")
icoLocDateStr = '2017/' + WINTER_MONTH + '/30 09:00:00'
icoDatetimeObjLA_winter = DateTimeUtil.dateTimeStringToArrowLocalDate(icoLocDateStr, LA_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printDate('LA', icoDatetimeObjLA_winter)

icoDatetimeObjNY = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_winter, NY_TIMEZONE)
printDate('NY', icoDatetimeObjNY)
printDate('LA copy', icoDatetimeObjLA_winter)

icoDatetimeObjZH = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_winter, ZH_TIMEZONE)
printDate('ZH', icoDatetimeObjZH)

icoDatetimeObjIN = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_winter, IN_TIMEZONE)
printDate('IN', icoDatetimeObjIN)

icoDatetimeObjUTC = DateTimeUtil.convertToTimeZone(icoDatetimeObjLA_winter, UTC_TIMEZONE)
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Placing summer orders --")
printDate('LA', icoDatetimeObjLA_summer)
orderDic = {}
normanOrderDateStr = '2017/' + SUMMER_MONTH + '/30 12:01:55'
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(normanOrderDateStr, NY_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('NO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_summer, orderDatetimeObj)

zoeOrderDateStr = '2017/' + SUMMER_MONTH + '/30 18:01:57'
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(zoeOrderDateStr, ZH_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('ZO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_summer, orderDatetimeObj)

indiraOrderDateStr = '2017/' + SUMMER_MONTH + '/30 21:32:07'
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(indiraOrderDateStr, IN_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('IN', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_summer, orderDatetimeObj)

print("\n-- Browsing summer orders --")
browseOrders(orderDic, LA_TIMEZONE)
browseOrders(orderDic, NY_TIMEZONE)
browseOrders(orderDic, IN_TIMEZONE)
browseOrders(orderDic, ZH_TIMEZONE)

print("\n-- Placing winter orders --")
printDate('LA', icoDatetimeObjLA_winter)
orderDic = {}
normanOrderDateStr = '2017/' + WINTER_MONTH + '/30 12:01:55'
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(normanOrderDateStr, NY_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('NO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_winter, orderDatetimeObj)

zoeOrderDateStr = '2017/' + WINTER_MONTH + '/30 18:01:57'
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(zoeOrderDateStr, ZH_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('ZO', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_winter, orderDatetimeObj)

indiraOrderDateStr = '2017/' + WINTER_MONTH + '/30 22:32:07' #note that India winter hour differs from summer hour !
orderDatetimeObj = DateTimeUtil.dateTimeStringToArrowLocalDate(indiraOrderDateStr, IN_TIMEZONE, DATE_TIME_FORMAT_ARROW)
printAndStoreOrderDateTS('IN', orderDatetimeObj, orderDic)
printLag(icoDatetimeObjLA_winter, orderDatetimeObj)

print("\n-- Browsing winter orders --")
browseOrders(orderDic, LA_TIMEZONE)
browseOrders(orderDic, NY_TIMEZONE)
browseOrders(orderDic, IN_TIMEZONE)
browseOrders(orderDic, ZH_TIMEZONE)