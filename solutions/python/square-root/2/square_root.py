def square_root(number:int) -> int:
     
    x = number
    for i in range(number):
       
        x = (1/2)*(x+(number/x))

    return int(x)