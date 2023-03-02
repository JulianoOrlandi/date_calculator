# Class:
class Date:
    def __init__ (self, year, month, day):

        # Checking for valid input:
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError("Parameters must be integers.")
        
        # Checking for valid input in year:
        if year < 1:
            raise ValueError("Year must be a positive integer.")
        
        # Checking for valid input in month:
        if month < 1 or month > 12:
            raise ValueError("Month must be a positive integer between 1 and 12.")
        
        # Checking for valid input in day:
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        if month in months_31:
            if day < 1 or day > 31:
                raise ValueError("Day is out of range for month.")
        elif month in months_30:
            if day< 1 or day > 30:
                raise ValueError("Day is out of range for month.")
        else:
            if is_leap(year):
                if day < 1 or day > 29:
                    raise ValueError("Day is out of range for month.")
            else:
                if day < 1 or day > 28:
                    raise ValueError("Day is out of range for month.")
        
        # Assigning attributes to object:
        self.year = year
        self.month = month
        self.day = day
        self.duration_in_days = convert_to_days(self)

    def __str__ (self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"
    
    def __sub__ (self, value):
        if isinstance(value, int):
            return(self.duration_in_days - value)
        elif isinstance(value, Date):
            return int(self.duration_in_days - value.duration_in_days)


# Functions:
def convert_to_days(date):
    year = date.year
    month = date.month
    day = date.day
    number_of_days = 0
    
    # Getting full years between date.year and year 1:
    year -= 1
    full_years = []
    while year > 0:
        full_years.append(year)
        year -= 1
    
    # Adding the full years' days to the number of days:
    for i in range(len(full_years)):
        if is_leap(full_years[i]):
            number_of_days += 366
        else:
            number_of_days += 365

    # Getting the full months between date.month and January of date.year:
    month -= 1
    full_months = []
    while month > 0:
        full_months.append(month)
        month -= 1
    
    # Adding the full months' days to number of days:
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    for i in range(len(full_months)):
        if full_months[i] in months_31:
            number_of_days += 31
        elif full_months[i] in months_30:
            number_of_days += 30
        else:
            if is_leap(date.year):
                number_of_days += 29
            else:
                number_of_days += 28

    # Adding the date.day to the number of days:
    day -= 1
    number_of_days += day

    return number_of_days


def is_leap(year):
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