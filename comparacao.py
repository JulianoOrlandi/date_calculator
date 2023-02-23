import datetime
import date_calculator


def main():   
    
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    
    for i in range(1, 2024):
        for j in range(1, 13):
            if j in months_31:
                for k in range(1, 32):
                    test_calc(i, j, k)            
            elif j in months_30:
                for k in range(1, 31):
                    test_calc(i, j, k)            
            else:
                if date_calculator.is_leap(i):
                    for k in range(1, 30):
                        test_calc(i, j, k)
                else:
                    for k in range(1, 29):
                        test_calc(i, j, k)
    
def test_calc(year, month, day):
    my_initial = date_calculator.Date(1, 1, 1)
    datetime_initial = datetime.date(1, 1, 1)
    my_date = date_calculator.Date(year, month, day)
    datetime_date = datetime.date(year, month, day)
    if (my_initial - my_date) != (datetime_initial - datetime_date).days:
        print("Erro")


if __name__ == "__main__":
    main()