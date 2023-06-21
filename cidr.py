from datetime import datetime, timedelta, time,date
   
pattern = '%d.%m.%Y %H:%M'
schedule = (
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=10), timedelta(hours=18)),
    (timedelta(hours=10), timedelta(hours=18))
)

client_time = datetime.strptime('02.11.2021 21:15', pattern)

if schedule[client_time.weekday()][0] <= timedelta(hours=client_time.hour,minutes=client_time.minute) <= schedule[client_time.weekday()][1]:
    print ((schedule[client_time.weekday()][1]-timedelta(hours=client_time.hour,minutes=client_time.minute)).seconds//60)
else:
    print("Магазин закрыт")