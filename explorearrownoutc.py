import arrow
from dateutil import tz

DATE_TIME_FORMAT_ARROW = 'YYYY/MM/DD HH:mm:ss'
DATE_TIME_FORMAT_TZ_ARROW = DATE_TIME_FORMAT_ARROW + ' ZZ'
SUMMER_MONTH = '09'
WINTER_MONTH = '11'

indiraOrderDateStr = '2017/' + SUMMER_MONTH + '/30 21:31:55'
print("\n-- Placing summer order --")
orderArrowObjIN = arrow.get(indiraOrderDateStr, DATE_TIME_FORMAT_ARROW).replace(tzinfo='Asia/Calcutta')
orderArrowObjUTC = orderArrowObjIN.to(tz.gettz('UTC'))
timeStamp = orderArrowObjIN.timestamp #timestamp is independant from timezone !
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('TS:  ' + str(timeStamp))

print("\n-- Browsing summer order --")
orderArrowObjIN = arrow.get(timeStamp).replace(tzinfo='Asia/Calcutta') #not working !! Most firt convert to UTC !
orderArrowObjIN = arrow.Arrow.utcfromtimestamp(timeStamp).to('Asia/Calcutta')
orderArrowObjUTC = orderArrowObjIN.to('UTC')
print('TS:  ' + str(timeStamp))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))

indiraOrderDateStr = '2017/' + WINTER_MONTH + '/30 21:31:55'
print("\n-- Placing winter order --")
orderArrowObjIN = arrow.get(indiraOrderDateStr, DATE_TIME_FORMAT_ARROW).replace(tzinfo='Asia/Calcutta')
orderArrowObjUTC = orderArrowObjIN.to(tz.gettz('UTC'))
timeStamp = orderArrowObjIN.timestamp
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('TS:  ' + str(timeStamp))

print("\n-- Browsing winter order --")
orderArrowObjIN = arrow.get(timeStamp).replace(tzinfo='Asia/Calcutta') #not working !! Most firt convert to UTC !
orderArrowObjIN = arrow.Arrow.utcfromtimestamp(timeStamp).to('Asia/Calcutta')
orderArrowObjUTC = orderArrowObjIN.to('UTC')
print('TS:  ' + str(timeStamp))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))

if __name__ == '__main__':
    pass