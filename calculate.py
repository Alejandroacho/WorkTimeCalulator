from datetime import timedelta


arrived_time = input('Enter the hour you arrived (ex 8:30): ')
dinner_time = input('Enter the hour you left for dinner (ex 14:30): ')
dinner_time_finished = input('Enter the hour you finished dinner (ex 15:30): ')
leaving_time = input('Enter the hour you left for work (ex 17:30): ')

arrived_hour = int(arrived_time.split(':')[0])
arrived_minute = int(arrived_time.split(':')[1])
arrived_time = timedelta(days=0, hours=arrived_hour, minutes=arrived_minute)

dinner_hour = int(dinner_time.split(':')[0])
dinner_minute = int(dinner_time.split(':')[1])
dinner_time = timedelta(days=0, hours=dinner_hour, minutes=dinner_minute)

dinner_end_hour = int(dinner_time_finished.split(':')[0])
dinner_end_minute = int(dinner_time_finished.split(':')[1])
dinner_end_time = timedelta(days=0, hours=dinner_end_hour, minutes=dinner_end_minute)

dinner_spend_time = dinner_end_time - dinner_time

leaving_hour = int(leaving_time.split(':')[0])
leaving_minute = int(leaving_time.split(':')[1])
leaving_time = timedelta(days=0, hours=leaving_hour, minutes=leaving_minute)

total_time_worked = leaving_time - arrived_time - dinner_spend_time

minutes, seconds = divmod(total_time_worked.seconds, 60)
hours, minutes = divmod(minutes, 60)
if minutes < 10:
    minutes = '0' + str(minutes)

print(f'Has trabajado {hours}:{minutes}h')
