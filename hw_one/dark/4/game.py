# coding: utf-8
from __future__ import division

def main():
    """
    Нахождение вариантов верных комбинаций выражения по заданному условию
    """ 

    while True:
        try:        
            num = abs(int(raw_input("Введите целое число: ")))
            break
        except ValueError:
            print "Введите целое число"

    numbers = ['%s'%n for n in range(1,10)]
    signs = '', '+', '-', '*', '/'
    
    signs_combs = [[p1,p2,p3,p4,p5,p6,p7,p8] for p1 in signs
                                            for p2 in signs
                                            for p3 in signs
                                            for p4 in signs
                                            for p5 in signs
                                            for p6 in signs
                                            for p7 in signs
                                            for p8 in signs]
                                            
    expressions = []
    count = 0
    
    for sg in signs_combs:
        expr_line = ""
        for tup in zip(numbers,sg):
            expr_line += "".join(tup)
        expressions.append(expr_line+'9')
    
    
    for exp in expressions:
        if eval(exp) == num: 
            print exp,"=",str(num)
            count += 1
    
    print count
        
if __name__ == "__main__":
    main()