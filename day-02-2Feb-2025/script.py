from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date(2025,1,1)
    d2 = date(2025,1,3)
    # result1 = diff_dates(d2, d1)
    diff=d2-d1
    # print('{} days between {} and {}'.format(result1, d1, d2))
    print(diff)
    print("Happy programmer's day!")

main()