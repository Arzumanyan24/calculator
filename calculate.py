def number():
   while True: 
        try:
            number= float(input('number:'))
            return number
        except ValueError:
            print("try again")


def choise():
    ch=('+','-','*','/')
    while True:
        try:
            c = input('+,-,/,* ')
            if c not in ch:
                    raise Exception
        except Exception:
            print('try again')
        else:
            return c
        

def result():
    x= number()
    
    c = choise()
    
    y= number()
    
    if c == "+":
        return x + y
    elif c == '-':
        return x - y
    elif c ==  '/':
        while True:
            try:
                res= x / y
                return res
            except ZeroDivisionError:
                print('not division')
                y = number()
print(result())