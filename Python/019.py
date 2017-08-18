import datetime
# months = {
#     1:31,
#     2:[28,29],
#     3:31,
#     4:30,
#     5:31,
#     6:30,
#     7:31,
#     8:31,
#     9:30,
#     10:31,
#     11:30,
#     12:31
# }
#
# #return True if it's a leap year
# def checkYear(n):
#     if(n%100==0):
#         #it is century
#         if(n%400==0):
#             return True
#         return False
#     elif (n%4==0):
#         return True
#     else:
#         return False

# 1 Jan 1900 was Monday
# What day is on 1 Jan 1901


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

print sundays
