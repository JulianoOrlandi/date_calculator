from date import Date, is_leap
from datetime import datetime, date
import time

# My algorithm: 90.9689 seconds
"""
start_time = time.monotonic()
for i in range(1, 1000):
    for j in range(1, 12):
        if j in [1, 3, 5, 7, 8, 10, 12]:
            for k in range(1, 32):
                Date(i, j, k) - Date(1, 1, 1)
        elif j in [4, 6, 9, 11]:
            for k in range(1, 31):
                Date(i, j, k) - Date(1, 1, 1)
        else:
            if is_leap(i):
                for k in range(1, 30):
                    Date(i, j, k) - Date(1, 1, 1)
            else:
                for k in range(1, 29):
                    Date(i, j, k) - Date(1, 1, 1)
end_time = time.monotonic()
print(end_time - start_time)
"""
# datetime module algorithm: 0.2969
start_time = time.monotonic()
for i in range(1, 1000):
    for j in range(1, 12):
        if j in [1, 3, 5, 7, 8, 10, 12]:
            for k in range(1, 32):
                date(i, j, k) - date(1, 1, 1)
        elif j in [4, 6, 9, 11]:
            for k in range(1, 31):
                date(i, j, k) - date(1, 1, 1)
        else:
            if is_leap(i):
                for k in range(1, 30):
                    date(i, j, k) - date(1, 1, 1)
            else:
                for k in range(1, 29):
                    date(i, j, k) - date(1, 1, 1)
end_time = time.monotonic()
print(end_time - start_time)
