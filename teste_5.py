import sys
import datetime
import math

def main():
    first_date = Datetime(1585, 3, 1)
    second_date = Datetime(1585, 4, 1)
    print("Date: ", first_date.getDatetime())
    print(microseconds_since_calendar_beginning(second_date))
    total_microseconds = 77673600000000 - microseconds_since_calendar_beginning(first_date)
    print(total_microseconds / 86400000000)




class Datetime:

    def __init__(self, year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0):
        
        # Checking for valid gregorian calendar date:
        if year < 1582:
            sys.exit("This calculator works only with the gregorian calendar. Dates must start from 1582-10-15.")
        elif year == 1582 and month < 10:
            sys.exit("This calculator works only with the gregorian calendar. Dates must start from 1582-10-15.")
        elif year == 1582 and month == 10 and day < 15:
            sys.exit("This calculator works only with the gregorian calendar. Dates must start from 1582-10-15.")
                    
        # Checking for valid input:
        if year <= 0 or not isinstance(year, int):
            sys.exit("Year must be a positive integer.")

        if month < 1 or month > 12 or not isinstance(month, int):
            sys.exit("Month must be an integer between 1 and 12.")
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31 or not isinstance(day, int):
                months_31_names = ["January", "March", "May", "July", "August", "October", "December"]
                month_index = [1, 3, 5, 7, 8, 10, 12].index(month)
                sys.exit(f"In {months_31_names[month_index]}, day must be a positive integer between 1 and 31.")
        
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30 or not isinstance(day, int):
                months_30_names = ["April", "June", "September", "November"]
                month_index = [4, 6, 9, 11].index(month)
                sys.exit(f"In {months_30_names[month_index]}, day must be a positive integer between 1 and 30.")
        else:
            if is_leap_year(year):
                if day < 1 or day > 29 or not isinstance(day, int):
                    sys.exit("In February of a leap year, day must be a positive integer between 1 and 29.")
            else:
                if day < 1 or day > 28 or not isinstance(day, int):
                    sys.exit("In February of a normal year, day must be a positive integer between 1 and 28.")
        
        if hour < 0 or hour > 23 or not isinstance(hour, int):
            sys.exit("Hour must be a positive integer between 0 and 23.")
        
        if minute < 0 or minute > 59 or not isinstance(minute, int):
            sys.exit("Minute must be a positive integer between 0 and 59.")
        
        if second < 0 or second > 59 or not isinstance(second, int):
            sys.exit("Second must be a positive integer between 0 and 59.")

        if microsecond < 0 or microsecond > 999999 or not isinstance(microsecond, int):
            sys.exit("Microsecond must be a positive integer between 0 and 999999.")
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond


    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
    
    def getDatetime(self):
        if self.microsecond != 0:
            return f"{self.year}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}:{self.second:02}.{self.microsecond:06}"
        else:
            return f"{self.year}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}:{self.second:02}"
    
    def extract_time(self):
        return Time(self.hour, self.minute, self.second, self.microsecond)

class Time():
    def __init__(self, hour = 0, minute = 0, second = 0, microsecond = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
    
    def getTime(self):
        if self.microsecond != 0:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02}.{self.microsecond:06}"
        else:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
                
    
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def convert_days_to_microseconds(days):
    return days * 86400000000

def convert_time_to_microseconds(time):
    hours_in_microseconds = time.hour * 3600000000
    minutes_in_microseconds = time.minute * 60000000
    seconds_in_microseconds = time.second * 1000000
    return time.microsecond + hours_in_microseconds + minutes_in_microseconds + seconds_in_microseconds

def microseconds_since_calendar_beginning(date):
        
        if date.year == 1582:
            if date.month == 12:
                full_months = []
                current_month = date.month - 1
                while current_month > 10:
                    full_months.append(current_month)
                    current_month -= 1
                
                number_of_days = 0
                months_31 = [1, 3, 5, 7, 8, 10, 12]
                months_30 = [4, 6, 9, 11]
                
                for month in full_months:
                    if month in months_31:
                        number_of_days += 31
                    elif month in months_30:
                        number_of_days += 30
                    elif month == 2 and is_leap_year(date.year) == True:
                        number_of_days += 29
                    else:
                        number_of_days += 28
                
                number_of_days = number_of_days + date.day - 1
            
                # Adding the number of days of October 1582:
                number_of_days += 17
                
            elif date.month == 11:
                number_of_days = date.day + 17 - 1
                
            else:
                number_of_days = date.day - 15
                
        else:
            
            # Getting the number of days since the beginning of date.year:
            full_months = []        
            current_month = date.month - 1        
            while current_month != 0:
                full_months.append(current_month)
                current_month -= 1
            
            number_of_days = 0
            months_31 = [1, 3, 5, 7, 8, 10, 12]
            months_30 = [4, 6, 9, 11]
            
            for month in full_months:
                if month in months_31:
                    number_of_days += 31
                elif month in months_30:
                    number_of_days += 30
                elif month == 2 and is_leap_year(date.year) == True:
                    number_of_days += 29
                else:
                    number_of_days += 28
                
            number_of_days = number_of_days + date.day - 1

            # Adding the number of days of 1582:
            number_of_days += 78

            # Getting the number of days of the year bewtween date.year and 1583:
            diff_in_years = date.year - 1583
            if diff_in_years > 0:

                # Getting the full_years from date.year to 1583, including 1583:
                full_years =[]
                first_year = date.year - 1
                while first_year > 1583:
                    full_years.append(first_year)
                    first_year = first_year - 1
                full_years.append(1583)
                
                # Adding the total days of each year in full_years:
                for year in full_years:
                    if is_leap_year(year):
                        number_of_days = number_of_days + 366
                    else:
                        number_of_days = number_of_days + 365

        return convert_days_to_microseconds(number_of_days) + convert_time_to_microseconds(date.extract_time())

def convert_microseconds_to_date(microseconds):
    # Getting the number of days:
    day = microseconds // 86400000000
    beginning_date = Datetime(1582, 10, 15)
    
    # To dates after 1582:
    # Updating year:
    if day > 77:
        
        beginning_date = Datetime(1583, 1, 1)
        day -= 78
        
        # Checking if beginning_date.year is a leap year:
        while day >= 365:
            if is_leap_year(beginning_date.year):
                if day >= 366:
                    beginning_date.year += 1
                    day -= 366
                else:
                    break
            else:
                if day >= 365:
                    beginning_date.year += 1
                    day -= 365

    # Incluir a lógica para datas em 1582:
    else:
        print("coisas a fazer")
        print(beginning_date.getDatetime())
    
    # Updating month:
    while True:
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]
        # Leap years:
        if is_leap_year(beginning_date.year):            
            if beginning_date.month in months_31:
                if day >= 31:
                    beginning_date.month += 1
                    day -= 31
                else:
                    break
            elif beginning_date.month in months_30:
                if day >= 30:
                    beginning_date.month += 1
                    day -= 30
                else:
                    break
            else:
                if day >= 29:
                    beginning_date.month += 1
                    day -= 29
                else:
                    break
        
        # Normal years:
        else:
            if beginning_date.month in months_31:
                if day >= 31:
                    beginning_date.month += 1
                    day -= 31
                else:
                    break
            elif beginning_date.month in months_30:
                if day >= 30:
                    beginning_date.month += 1
                    day -= 30
                else:
                    break
            else:
                if day >= 28:
                    beginning_date.month += 1
                    day -= 28
                else:
                    break
    
    # Updating day:
    beginning_date.day += day

    # Getting the remaining time:
    hour = (((microseconds / 86400000000) % 1) * 24)
    hour_final = hour // 1
    minute = (hour % 1) * 60
    minute_final = minute // 1
    second = (minute % 1) * 60
    second_final = second // 1
    microsecond_final = (second % 1) * 1000000
    new_date = Datetime(beginning_date.year, beginning_date.month, beginning_date.day, int(hour_final), int(minute_final), int(second_final), int(microsecond_final))
    print("Date: ", new_date.getDatetime())
    
    return 0




if __name__ == "__main__":
    main()