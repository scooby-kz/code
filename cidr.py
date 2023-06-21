from datetime import datetime, timedelta, time,date
   
def num_of_sundays(year1):
    start = datetime(year=year1,month=1,day=1)
    end = datetime(year=year1,month=12,day=31)
    lst = ([start.toordinal(), end.toordinal()])
    sun = 0
    for i in range (lst[0],lst[1]):
        if date.fromordinal(i).isoweekday() == 6:
            sun += 1
    return (sun)

print(num_of_sundays(2022))