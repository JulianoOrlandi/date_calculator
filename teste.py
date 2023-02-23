

# Convert a string to a datetime object:

def main():
    example = Datetime(23, 59, 59, 999)
    #print(example.getDatetime())
    miliseconds = example.convert_to_miliseconds()
    miliseconds_result, seconds_result, minutes_result, hours_result = convert_to_datetime(miliseconds)
    print(miliseconds_result)
    print(seconds_result)
    print(minutes_result)
    print(hours_result)


class Datetime:

    def __init__(self, hour, minute, second, milisecond):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.milisecond = milisecond
    
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute
    
    def getSecond(self):
        return self.second
    
    def getMilisecond(self):
        return self.milisecond
    
    def getDatetime(self):
        return  f"{self.hour:02d}" + ":" + f"{self.minute:02d}" + ":" + f"{self.second:02d}" + ":" + f"{self.milisecond:04d}"

    def convert_to_miliseconds(self):
        hour_in_mili = self.hour * 3600000
        minute_in_mili = self.minute * 60000
        second_in_mili = self.second * 1000
        return hour_in_mili + minute_in_mili + second_in_mili + self.milisecond

def convert_to_datetime(miliseconds):
    miliseconds_result = int(((miliseconds / 1000) % 1) * 1000)

    seconds = (miliseconds / 1000) - ((miliseconds / 1000) % 1)
    seconds_result = int(((seconds / 60) % 1) * 60)
    
    minutes = (seconds / 60) - ((seconds / 60) % 1)
    minutes_result = int(((minutes / 60) % 1) * 60)

    hours_result = int((minutes / 60) - ((minutes / 60) % 1))
    
    return miliseconds_result, seconds_result, minutes_result, hours_result

if __name__ == "__main__":
    main()