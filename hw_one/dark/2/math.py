# coding: utf-8

def gcd(a,b):
    while b > 0: a,b = b, a%b
    return a
    
def lcm (a,b):
    return a * b / gcd(a, b)
    
def prime(num):
    for x in range (2, int(num**0.5+1)):    
        if num%x == 0:  
            return 0
    return 1
        
def prime_list(last):
    for val in range(2, last):
        if prime(val):
            print val

def main():
    """
    Математические задачки
    """
    print "\n0 - Наименьшее общее кратное\n1 - Наибольший общий делитель\n2 - Список простых чисел до заданного значения"
    while True:
        try:
            x = int(raw_input(": "))
            if 0 <= x <= 2:
                break
        except ValueError:
            print "Введите целое число"
    
    if x < 2:
        while True:
            try:        
                y = [abs(int(num)) for num in raw_input("Введите 2 целых числа через пробел: ").split()]
                if len(y) == 2:
                    break
            except ValueError:
                print "Введите 2 целых числа"
        if x == 0:
            print lcm(y[0],y[1])
        else:
            print gcd(y[0],y[1])
    else:
        while True:
            try:        
                num = abs(int(raw_input("Введите границу: ")))
                break
            except ValueError:
                print "Введите целое число"

        prime_list(num)
        
if __name__ == "__main__":
    main()