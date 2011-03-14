# coding: utf-8

def factorial(num):
    print reduce(lambda x, y: x*y, xrange(1,num+1), 1)

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b
        
def fib_list(num):
    f = fib()
    for i in xrange(num):
        print f.next()
        
def sqrt_fun(num):
    print "%f" % num**0.5

def main():
    """
    Крутые математические задачки
    """
    print "\n0 - Факториал\n1 - Ряд Фибоначчи\n2 - Квадратный корень"
    while True:
        try:
            x = int(raw_input(": "))
            if 0 <= x <= 2:
                break
        except ValueError:
            print "Введите число"
    

    while True:
        try:        
            num = abs(int(raw_input("Введите целое число: ")))
            break
        except ValueError:
            print "Введите целое число"

    if x == 0:
        factorial(num)
    elif x == 1:
        fib_list(num)
    else:
        sqrt_fun(num)
        
if __name__ == "__main__":
    main()