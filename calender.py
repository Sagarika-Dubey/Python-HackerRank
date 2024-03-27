import calendar
def get_the_day_of_the_month(date): 
    month,day,year = map(str, date.split(' '))
    day_of_the_week = calendar.weekday(int(year),int(month),int(day))
    day_name = calendar.day_name[day_of_the_week]
    print(day_name.upper())


date = input()
get_the_day_of_the_month(date)