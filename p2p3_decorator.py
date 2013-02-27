from time import time, sleep
from datetime import datetime

_SNAIL_MESSAGE_FORMAT = 'Function <%(fctName)s> took %(duration)f seconds [started @ %(startTime)s, end @ %(endTime)s].'

def snail(fct, threshold=None):
    def generateOutput(startTime, endTime):
        startTimeDt = datetime.fromtimestamp(startTime)
        endTimeDt = datetime.fromtimestamp(endTime)
        outputDetails = {'fctName': fct.func_name,
                         'duration': endTime - startTime,
                         'startTime': startTimeDt.strftime(
                             '%d.%m.%Y %H:%M:%S.%f'),
                         'endTime': endTimeDt.strftime(
                             '%d.%m.%Y %H:%M:%S.%f')}
        return _SNAIL_MESSAGE_FORMAT % outputDetails

    def wrapper():
        startTime = time()
        fct()
        endTime = time()
        print generateOutput(startTime, endTime)

    return wrapper

@snail
def slowFunction():
    sleep(2.45)


if __name__ == '__main__':
    slowFunction()

