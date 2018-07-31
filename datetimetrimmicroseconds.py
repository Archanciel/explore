from datetime import datetime

now = datetime.now()
print(now)
print(now.timestamp())
nowAtSecond = now.replace(microsecond=0)
print(nowAtSecond)
print(nowAtSecond.timestamp())



if __name__ == '__main__':
    pass