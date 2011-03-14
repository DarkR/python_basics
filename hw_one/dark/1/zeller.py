# coding: utf-8
import sys

def main():
    """
    Day of Week finder. Usage: day month year.
    Example: python zeller.py 30 11 1987
    """
    
    try:
        int_date = [abs(int(arg)) for arg in sys.argv[1:]]
    except ValueError:
        print "Введите дату из целых чисел"
        return
    days_of_week = ("Суббота","Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница")
    K = int_date[2]%100
    J = int_date[2]/100
    print days_of_week[(int_date[0] + 26*(int_date[1]+1)/10 + K + K/4 + J/4 - 2*J)%7]

if __name__ == "__main__":
    main()