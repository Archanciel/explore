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
timeStampUTC = orderArrowObjUTC.timestamp
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('TS:  ' + str(timeStampUTC) + '-utc ' + str(orderArrowObjIN.timestamp) + '-in')

print("\n-- Browsing summer order --")
orderArrowObjUTC = arrow.get(timeStampUTC).replace(tzinfo='UTC')
orderArrowObjIN = orderArrowObjUTC.to('Asia/Calcutta')
#orderArrowObjIN = arrow.Arrow.utcfromtimestamp(timeStampUTC).to('Asia/Calcutta') works too !
print('TS:  ' + str(timeStampUTC) + '-utc ' + str(orderArrowObjIN.timestamp) + '-in')
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))

indiraOrderDateStr = '2017/' + WINTER_MONTH + '/30 21:31:55'
print("\n-- Placing winter order --")
orderArrowObjIN = arrow.get(indiraOrderDateStr, DATE_TIME_FORMAT_ARROW).replace(tzinfo='Asia/Calcutta')
orderArrowObjUTC = orderArrowObjIN.to(tz.gettz('UTC'))
timeStampUTC = orderArrowObjUTC.timestamp
timeStampIN = orderArrowObjIN.timestamp
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('TS:  ' + str(timeStampUTC) + '-utc ' + str(timeStampIN) + '-in')

print("\n-- Browsing winter order --")
orderArrowObjUTC = arrow.get(timeStampUTC).replace(tzinfo='UTC')
orderArrowObjIN = orderArrowObjUTC.to('Asia/Calcutta')
#orderArrowObjIN = arrow.Arrow.utcfromtimestamp(timeStampUTC).to('Asia/Calcutta') works too !
print('TS:  ' + str(timeStampUTC) + '-utc ' + str(timeStampIN) + '-in')
print('UTC: ' + orderArrowObjUTC.format(DATE_TIME_FORMAT_TZ_ARROW))
print('IN:  ' + orderArrowObjIN.format(DATE_TIME_FORMAT_TZ_ARROW))

if __name__ == '__main__':
    pass