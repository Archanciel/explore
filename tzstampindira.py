import time
from datetime import datetime

from pytz import timezone

'''
Indira in India places an
order on a Los Angeles ICO which 
starts on Sept (Nov) 30th, 2017 at 9.00
PDT time.

The order are stored with a UTC
time stamp in the ICO database.

It is be accessed by Indira
using her browser.

A problem pops up în the case the order
is placed in november: browsing the placed
order displays it with a time which is 1 hour
too late !
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
SUMMER_MONTH = '09'
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

def browseOrders(orderDic, viewerTimezone, tsCorr):
    print('--Orders {}--'.format(viewerTimezone))
    for key, value in orderDic.items():
        localDateStr, dst = timestamp2localdate(value, viewerTimezone, tsCorr)
        #print('dst-->{}'.format(dst))
        print("{} {} {} d-{}".format(key, value, localDateStr, dst))
    print('')   

def timestamp2localdate(strTimestamp, localTimeZone, tsCorr):
    # function converts a UTC timestamp into timezone Gregorian date
    intTimeStamp = int(strTimestamp)
    intTimeStamp -= tsCorr 
    datetimeUTC = datetime.fromtimestamp(intTimeStamp).replace(tzinfo=timezone('UTC'))
    datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
    datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
    datetimeLocal = datetimeUTC.astimezone(timezone(localTimeZone))
    dst = str(datetimeLocal.timetuple()[8])
    print('tsCorr: {} dst-->{}'.format(tsCorr,dst))
    return datetimeLocal.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR), dst

'''
print("-- Summer ICO start date/time --")
icoLocDateStr = '2017/' + MONTH + '/30 09:00:00'
icoDatetimeObjUnlocalized = datetime.strptime(icoLocDateStr, DATE_TIME_FORMAT)
icoDatetimeObjLA = timezone(LA_TIMEZONE).localize(icoDatetimeObjUnlocalized)
printDate('LA', icoDatetimeObjLA)

icoDatetimeObjNY = icoDatetimeObjLA.astimezone(timezone(NY_TIMEZONE))
printDate('NY', icoDatetimeObjNY)
icoDatetimeObjUTC = icoDatetimeObjLA.astimezone(timezone(UTC_TIMEZONE))
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Placing summer order --")

printDateNoDst('LA', icoDatetimeObjLA)
normanOrderDateStr = '2017/' + MONTH + '/30 12:01:55'
orderDatetimeObjUnlocalized = datetime.strptime(normanOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObjNY = timezone(NY_TIMEZONE).localize(orderDatetimeObjUnlocalized)
print('NO:  ' + orderDatetimeObjNY.strftime(DATE_TIME_FORMAT_TZ))
datetimeObjUTC = orderDatetimeObjNY.astimezone(timezone(UTC_TIMEZONE))
timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
timeStampStrNO_UTC = str(int(timeStampUTC))
print('     UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
print('     TS:  ' + timeStampStrNO_UTC)
printLag(icoDatetimeObjLA, orderDatetimeObjNY)

print("\n-- Browsing summer orders --")

print('--Order {}--'.format(NY_TIMEZONE))
intTimeStamp = int(timeStampStrNO_UTC)
dstNY = orderDatetimeObjNY.timetuple()[8]
tsCorrFactor = TIMESTAMP_TO_DATE_CORRECTION_FACTOR * dstIN
intTimeStamp -= tsCorrFactor
datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
datetimeLocal = datetimeUTC.astimezone(timezone(NY_TIMEZONE))

dstNYStr = str(dstNY)
print('tsCorr: {} dst-->{}'.format(TIMESTAMP_TO_DATE_CORRECTION_FACTOR, dstNYStr))
localDateStr = datetimeLocal.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR)
print("{} {} {} d-{}".format('NO', timeStampStrNO_UTC, localDateStr, dstNYStr))
'''





print("-- Summer ICO start date/time --")
icoLocDateStr = '2017/' + SUMMER_MONTH + '/30 09:00:00'
icoDatetimeObjUnlocalized = datetime.strptime(icoLocDateStr, DATE_TIME_FORMAT)
icoDatetimeObjLA = timezone(LA_TIMEZONE).localize(icoDatetimeObjUnlocalized)
printDate('LA', icoDatetimeObjLA)

icoDatetimeObjIN = icoDatetimeObjLA.astimezone(timezone(IN_TIMEZONE))
printDate('IN', icoDatetimeObjIN)
icoDatetimeObjUTC = icoDatetimeObjLA.astimezone(timezone(UTC_TIMEZONE))
printDate('UTC', icoDatetimeObjUTC)

'''
print("\n-- Placing summer order --")

printDateNoDst('LA', icoDatetimeObjLA)
indiraOrderDateStr = '2017/' + MONTH + '/30 21:31:55'
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObjIN = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
print('IN:  ' + orderDatetimeObjIN.strftime(DATE_TIME_FORMAT_TZ))
datetimeObjUTC = orderDatetimeObjIN.astimezone(timezone(UTC_TIMEZONE))
timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
timeStampStrIN_UTC = str(int(timeStampUTC))
print('     UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
print('     TS:  ' + timeStampStrIN_UTC)
printLag(icoDatetimeObjLA, orderDatetimeObjIN)

print("\n-- Browsing summer orders --")

print('--Order {}--'.format(IN_TIMEZONE))
intTimeStamp = int(timeStampStrIN_UTC)
dstIN = orderDatetimeObjIN.timetuple()[8]
tsCorrFactor = TIMESTAMP_TO_DATE_CORRECTION_FACTOR * dstIN
intTimeStamp -= tsCorrFactor
datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
datetimeLocal = datetimeUTC.astimezone(timezone(IN_TIMEZONE))

dstINStr = str(dstIN)
print('tsCorr: {} dst-->{}'.format(tsCorrFactor, dstINStr))
localDateStr = datetimeLocal.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR)
utcDateStr = datetimeUTC.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR)
print('{} {} {} '.format('UTC', timeStampStrIN_UTC, utcDateStr))
print("{}  {} {} d-{}".format('IN', str(intTimeStamp), localDateStr, dstINStr))


print("\n-- Winter ICO start date/time --")
icoLocDateStr = '2017/' + WINTER_MONTH + '/30 09:00:00'
icoDatetimeObjUnlocalized = datetime.strptime(icoLocDateStr, DATE_TIME_FORMAT)
icoDatetimeObjLA = timezone(LA_TIMEZONE).localize(icoDatetimeObjUnlocalized)
printDate('LA', icoDatetimeObjLA)

icoDatetimeObjIN = icoDatetimeObjLA.astimezone(timezone(IN_TIMEZONE))
printDate('IN', icoDatetimeObjIN)
icoDatetimeObjUTC = icoDatetimeObjLA.astimezone(timezone(UTC_TIMEZONE))
printDate('UTC', icoDatetimeObjUTC)

print("\n-- Placing winter order --")

printDateNoDst('LA', icoDatetimeObjLA)
indiraOrderDateStr = '2017/' + WINTER_MONTH + '/30 22:31:55'
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObjIN = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
print('IN:  ' + orderDatetimeObjIN.strftime(DATE_TIME_FORMAT_TZ))
datetimeObjUTC = orderDatetimeObjIN.astimezone(timezone(UTC_TIMEZONE))
timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
timeStampStrIN_UTC = str(int(timeStampUTC))
print('     UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
print('     TS:  ' + timeStampStrIN_UTC)
printLag(icoDatetimeObjLA, orderDatetimeObjIN)

print("\n-- Browsing winter orders --")

print('--Order {}--'.format(IN_TIMEZONE))
intTimeStamp = int(timeStampStrIN_UTC)
dstIN = orderDatetimeObjIN.timetuple()[8]
tsCorrFactor = TIMESTAMP_TO_DATE_CORRECTION_FACTOR * dstIN
intTimeStamp -= tsCorrFactor
datetimeUnlocalized = datetime.fromtimestamp(intTimeStamp)
datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
datetimeLocal = datetimeUTC.astimezone(timezone(IN_TIMEZONE))

dstINStr = str(dstIN)
print('tsCorr: {} dst-->{}'.format(tsCorrFactor, dstINStr))
localDateStr = datetimeLocal.strftime(DATE_TIME_FORMAT_TZ_NO_YEAR)
print("{} {} {} d-{}".format('IN', timeStampStrIN_UTC, localDateStr, dstINStr))
'''

print("\n-- Placing summer order --")
indiraOrderDateStr = '2017/' + SUMMER_MONTH + '/30 21:31:55'
orderDatetimeObjUnlocalized = datetime.strptime(indiraOrderDateStr, DATE_TIME_FORMAT)
orderDatetimeObjIN = timezone(IN_TIMEZONE).localize(orderDatetimeObjUnlocalized)
datetimeObjUTC = orderDatetimeObjIN.astimezone(timezone(UTC_TIMEZONE))
timeStampUTC = time.mktime(datetimeObjUTC.timetuple())
print('IN:  ' + orderDatetimeObjIN.strftime(DATE_TIME_FORMAT_TZ))
print('UTC: ' + datetimeObjUTC.strftime(DATE_TIME_FORMAT_TZ))
print('     TS:  ' + str(timeStampUTC))

print("\n-- Browsing summer order --")
datetimeUnlocalized = datetime.fromtimestamp(timeStampUTC)
datetimeUTC = timezone(UTC_TIMEZONE).localize(datetimeUnlocalized)
datetimeIN = datetimeUTC.astimezone(timezone(IN_TIMEZONE))
print('{}: {}'.format('UTC', datetimeUTC.strftime(DATE_TIME_FORMAT_TZ)))
print('     TS:  ' + str(timeStampUTC))
print("{}:  {}".format('IN', datetimeIN.strftime(DATE_TIME_FORMAT_TZ)))
