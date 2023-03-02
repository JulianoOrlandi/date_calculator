import pytest
from date import Date, convert_to_days, is_leap
import datetime

def test_date_init():
    with pytest.raises(TypeError):
        Date('a', 1, 1)
    with pytest.raises(TypeError):
        Date(1, 'a', 1)
    with pytest.raises(TypeError):
        Date(1, 1, 'a')
    with pytest.raises(ValueError):
        Date(-1, 1, 1)
    with pytest.raises(ValueError):
        Date(1, 25, 1)
    with pytest.raises(ValueError):
        Date(1999, 2, 29)

def test_date_str():
    assert str(Date(1982, 11, 23)) == str(datetime.date(1982, 11, 23))

def test_date_sub():
    for i in range(1, 2024):
        for j in range(1, 13):
            if j in [1, 3, 5, 7, 8, 10, 12]:
                for k in range(1, 32):
                    assert Date(i, j, k) - Date(1, 1, 1) == (datetime.date(i, j, k) - 
                                                             datetime.date(1, 1, 1)).days
            elif j in [4, 6, 9, 11]:
                for k in range(1, 31):
                    assert Date(i, j, k) - Date(1, 1, 1) == (datetime.date(i, j, k) - 
                                                             datetime.date(1, 1, 1)).days
            else:
                if is_leap(i):
                    for k in range(1, 30):
                        assert Date(i, j, k) - Date(1, 1, 1) == (datetime.date(i, j, k) - 
                                                                 datetime.date(1, 1, 1)).days
                else:
                    for k in range(1, 29):
                        assert Date(i, j, k) - Date(1, 1, 1) == (datetime.date(i, j, k) - 
                                                                 datetime.date(1, 1, 1)).days

def test_is_leap():
    assert is_leap(2000) == True
    assert is_leap(2001) == False
    assert is_leap(1900) == False

def test_convert_to_days():
    assert convert_to_days(Date(1982, 11, 23)) == 723871