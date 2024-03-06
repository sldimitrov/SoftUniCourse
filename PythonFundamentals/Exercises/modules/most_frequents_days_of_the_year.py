from calendar import weekday
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def most_frequent_days(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    if beg == end:
        return [week[beg]]
    else:
        if beg < end:
            return [week[beg], week[end]]
        else:
            return [week[end], week[beg]]


print(most_frequent_days(2023))