import arrow


class DateTimeUtil:
    @staticmethod
    def timeStampToArrowLocalDate(timeStamp, timeZoneStr):
        '''
        FGiven a UTC/GMT timezone independent timestamp and a timezone string specification,
        returns a localized arrow object.

        :param timeStamp: UTC/GMT timezone independent timestamp
        :param timeZoneStr: like 'Europe/Zurich' or 'US/Pacific'
        :return: arrow localized date time object
        '''
        return arrow.Arrow.utcfromtimestamp(timeStamp).to(timeZoneStr)


    @staticmethod
    def dateTimeStringToTimeStamp(dateTimeStr, timeZoneStr, dateTimeFormatArrow):
        '''
        Given a datetime string which format abide to to the passed arrow format and
        a timezone string specification, return a UTC/GMT timezone independent timestamp.

        :param dateTimeStr:
        :param timeZoneStr: like 'Europe/Zurich' or 'US/Pacific'
        :param dateTimeFormatArrow: example YYYY/MM/DD HH:mm:ss --> 2017/09/12 15:32:21
        :return: int UTC/GMT timezone independent timestamp
        '''
        arrowObj = arrow.get(dateTimeStr, dateTimeFormatArrow).replace(tzinfo=timeZoneStr)

        return arrowObj.timestamp  # timestamp is independant from timezone !


    @staticmethod
    def dateTimeStringToArrowLocalDate(dateTimeStr, timeZoneStr, dateTimeFormatArrow):
        '''
        Given a datetime string which format abide to to the passed arrow format and
        a timezone string specification, return an arrow localized date time object.

        :param dateTimeStr:
        :param timeZoneStr: like 'Europe/Zurich' or 'US/Pacific'
        :param dateTimeFormatArrow: example YYYY/MM/DD HH:mm:ss --> 2017/09/12 15:32:21
        :return: arrow localized date time object
        '''
        return arrow.get(dateTimeStr, dateTimeFormatArrow).replace(tzinfo=timeZoneStr)


    @staticmethod
    def convertToTimeZone(dateTimeArrowObject, timeZoneStr):
        '''
        Return the passed dateTimeArrowObject converted to the passed timeZoneStr.

        :param dateTimeArrowObject: arrow localized date time object.
        :param timeZoneStr: like 'Europe/Zurich' or 'US/Pacific'
        :return: arrow date time object localized  to passed timeZoneStr
        '''
        return dateTimeArrowObject.to(timeZoneStr)


if __name__ == '__main__':
    pass