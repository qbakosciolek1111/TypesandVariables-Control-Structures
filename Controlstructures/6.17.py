###
# Converts time from 24-hour format (hh:mm) to 12-hour format
#
time_24 = input('Enter time (24-hour format): ')
hour_text, minutes = time_24.split(':') 
hour = int(hour_text)  

if hour >= 12:  
    suffix = 'pm'
else:
    suffix = 'am'

hour_12 = hour % 12  
if hour_12 == 0:  
    hour_12 = 12

print(f'Time in 12-hour format: {hour_12}:{minutes}{suffix}')