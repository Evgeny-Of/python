sec = int(input('Ведите время в секундах: '))

hour = (sec / 86400 - int(sec / 86400)) * 24
minute = (hour - int(hour)) * 60
second = (minute - int(minute)) * 60

# s_hour = ''
# s_minute = ''
# s_second = ''
#
if round(minute) < 10:
    minute = '0%s' % round(minute)
else:
    minute = round(minute)
if round(second) < 10:
    second = '0%s' % round(second)
else:
    second = round(second)
if round(hour) < 10:
    hour = '0%s' % round(hour)
else:
    hour = round(hour)
if hour == 24:
    print('Формат отображения точного времени превысил сутки (24 часа)')
else:
    string1 = f'{hour}:{minute}:{second}'
    print(string1)
