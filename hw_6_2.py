number = int(input('Enter a number between 0 and 8640000: '))

days, sec_balance_hour = divmod(number, (24 * 60 * 60))
hour, sec_balance_minute = divmod(sec_balance_hour, 3600)
minute, sec = divmod(sec_balance_minute, 60)

if 11 <= days % 100 <= 14:
    result_day = 'днів'
elif days % 10 == 1:
    result_day = 'день'
elif days % 10 in(2, 3, 4):
    result_day = 'дні'
else:
    result_day = 'днів'

print(f'{days} {result_day}, {str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}')