import datetime
import time
# #return True if it's a leap year
def checkYear(n):
    if(n%100==0):
        #it is century
        if(n%400==0):
            return True
        return False
    elif (n%4==0):
        return True
    else:
        return False

def setDays(leap,month):
    if month==4 or month==6 or month==9 or month==11:
        return 30
    elif (month==2 and leap):
        return 29
    elif (month==2 and not leap):
        return 28
    else:
        return 31

def countSundays():
    print "Without Any Extensive Modules"
    dW = 2 # value from 1 to 7, 1-1-1901 was Tuesday
    counter = 0
    for y in range(1901,2001):
        leap = checkYear(y)
        for m in range(1,13):
            days = setDays(leap,m)
            for d in range(1, days+1):
                if(d==1 and dW==7):
                    counter+=1
                #after Sunday reset counter to Monday
                dW+=1
                if (dW==8): dW=1
    print "Sundays: %d" % counter





# 1 Jan 1900 was Monday
# What day is on 1 Jan 1901
def calcDateTime():
    print "Using datetime library"
    start_date = datetime.date(1901,1,1)
    d = start_date
    end_date = datetime.date(2000,12,31)
    delta = datetime.timedelta(days=1)
    sundays = 0

    while d <= end_date:
        if(d.day==1):
            if(d.weekday()==6):
                sundays+=1
        d+=delta

    print "Sundays: %d" % sundays

start_time=time.time()
countSundays()
total_time = time.time() - start_time
print "TIME: ", total_time

print ""

start_time=time.time()
calcDateTime()
total_time = time.time() - start_time
print "TIME: ", total_time
