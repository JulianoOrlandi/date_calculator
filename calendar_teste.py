from datetime import datetime
import sys
# Getting all the leap years from 1582 a.d.:
'''
start_year = 1582
end_year = 2023
years = [1582]

for i in range(end_year - start_year):
    years.append(years[i] + 1)
leap_years = []

for i in range(len(years)):
    if (years[i] / 4) % 1 == 0:
        if (years[i] / 100) % 1 != 0:
            leap_years.append(years[i])
        else:
            if (years[i] / 400) % 1 == 0:
                leap_years.append(years[i])

print(leap_years)
print(len(leap_years))
start_year = 1585
next_year = 1588
difference = (next_year - start_year)

print(difference * 365.2425)
'''
def main():

    x = Time(31, 12, 59, 59)
    print(x.getTime())
    print(x.convert_to_seconds())
    y = convert_to_time(x.convert_to_seconds())
    print(y.getTime())
    
class Time:
    def __init__(self, days, hours, minutes, seconds):
        if days > 31 or days < 0:
            sys.exit("Invalid days.")
        if hours > 23 or hours < 0:
            sys.exit("Invalid hour.")
        elif minutes > 59 or minutes < 0:
            sys.exit("Invalid minutes.")
        elif seconds > 59 or seconds < 0:
            sys.exit("Invalid seconds.")
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getDays(self):
        return self.days
    
    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes
    
    def getSeconds(self):
        return self.seconds

    def getTime(self):
        return str(str(self.days) + " " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
    
    def convert_to_seconds(self):
        days_in_seconds = self.getDays() * 86400 
        hour_in_seconds = self.getHours() * 3600
        minutes_in_seconds = self.getMinutes() * 60
        return days_in_seconds + hour_in_seconds + minutes_in_seconds + self.getSeconds()
    
def convert_to_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    hours_int = int(hours - (hours % 1))
    minutes = (hours % 1) * 60
    minutes_int = int(minutes - (minutes % 1))
    seconds_int = int((minutes % 1) * 60)
    
    return Time(hours_int, minutes_int, seconds_int)

#def time_diff(tempo_2, tempo_1):
    #print(convert_to_seconds(tempo_2))

if __name__ == "__main__":
    main()

#time_a = "01:30:30"
#time_b = "01:00:35"
