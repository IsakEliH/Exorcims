def is_valid(isbn:str) -> bool:

    isbn = isbn.replace('-','')
    if len(isbn) != 10:
        return False 

    new_isbn = []
    for i in isbn:
        if i.upper() == "X" and i == isbn[-1]:
            new_isbn.append(10)
        elif i.isdigit():
            new_isbn.append(int(i))

    if len(new_isbn) != 10:
        return False 

    def new(x): return int(new_isbn[x])

    return (new(0) * 10 + new(1) * 9 + new(2) * 8 + new(3) * 7 + new(4) * 6 + new(5) * 5 + new(6) * 4 + new(7) * 3 + new(8) * 2 + new(9) * 1) % 11 == 0