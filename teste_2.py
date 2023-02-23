import sys
import datetime

def main():

    # Creating two date objects with datetime module:
    date_1 = datetime.datetime(2001, 2, 1, 12, 59, 0)
    date_2 = datetime.datetime(2011, 2, 2, 23, 59, 59, 999999)

    # Creating two date objects with my class:
    date_3 = Date(2001, 2, 1, 23, 59, 0)
    date_4 = Date(2001, 2, 2, 23, 59, 0)

    #print(number_of_days_since_jan_1(date_3))
    
    print(date_2 + datetime.timedelta(microseconds=2))
    # Subtracting dates with datetime module:
    #print(date_2 - date_1)
    
    # Subtracting dates with my function:
    #print(difference_in_days(date_4, date_3))

    #date_2 = Date(2022, 9, 30, 12, 30, 0)
    #print(date_2.getDatetime())
    #date_2 = Date(2023, 1, 1, 23, 59)    
    #print(difference_in_days(date_2, date_1))
    #print(date_2.getDatetime())
    print()

class Date:

    def __init__(self, year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0):
        
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

    def getLeap(self):
        return self.leap
    
    def getDatetime(self):
        if self.microsecond != 0:
            return f"{self.year}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}:{self.second:02}.{self.microsecond:06}"
        else:
            return f"{self.year}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}:{self.second:02}"
    def getNumber_of_days_since_jan_1(self):
        return self.number_of_days_since_jan_1
    
    def getNumber_of_days_to_dec_31(self):
        return self.number_of_days_to_dec_31
    
def number_of_days_since_jan_1(date):
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
            elif month == 2 and date.leap == True:
                number_of_days += 29
            else:
                number_of_days += 28
            
        return number_of_days + date.day

def number_of_days_to_dec_31(date):
        
        if is_leap_year(date.year) == True:
            number_of_days_to_dec_31 = 366 - number_of_days_since_jan_1(date)
        else: 
            number_of_days_to_dec_31 = 365 - number_of_days_since_jan_1(date)
        
        return number_of_days_to_dec_31


def difference_in_days(date_2, date_1):
    end_year_done_days = number_of_days_since_jan_1(date_2)
    start_year_missing_days = number_of_days_to_dec_31(date_1)
    difference_in_days = end_year_done_days + start_year_missing_days
    full_years = []
    first_year = (date_2.getYear()) - 1
    last_year = (date_1.getYear())
    while first_year != last_year:
        full_years.append(first_year)
        first_year -= 1
    
    for item in full_years:
        if is_leap_year(item):
            difference_in_days = difference_in_days + 366
        else:
            difference_in_days = difference_in_days + 365
    
    if date_1.year == 1582 and date_1.month <= 10 and date_1.day <= 14:
        difference_in_days = difference_in_days - 10

    return difference_in_days

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

if __name__ == "__main__":
    main()