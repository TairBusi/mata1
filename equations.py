def exponent(x:float) ->float:
    i=1
    numerator=1
    assembly = 1
    answer = 1
    while (i < 100):
        numerator= numerator*x
        assembly= assembly*i
        answer= answer*(numerator/assembly)
        i=i+1
        return answer
    
def Ln(x:float) ->float:
    i=1
    y=1
    while (i < 100):
        y=y+(2*((x-exponent(y))/(x+exponent(y))))
        i=i+1
    return y

def XtimesY(x:float,y: float) -> float:
    if x>0:
        sum_= exponent(y*Ln(x))
        return sum_
    else:
        x=((-1)*x)
        if (x%2 == 0):
            sum_= exponent(y*Ln(x))
            return sum_
        else: 
            sum_= exponent(y*Ln(x))
            return ((-1)*sum_)

def sqrt(x:float,y:float) -> float:
    sqr_= XtimesY(x,(1/y))
    return sqr_

def calculate(x: float) -> float:
    sum_num = (XtimesY(2.71828182846, x)*XtimesY(7, x)*XtimesY(x,-1))
    return float('%0.6f' % sum_num)




    
    