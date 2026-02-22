def is_isogram(string:str) -> bool:
    uppercase = string.upper()
    

    isogram_set = set()
    special = []

    for i in uppercase:
        if i == " " or i == "-":
            special.append(i)
        else:
            isogram_set.add(i)

    length = len(isogram_set)

    length += len(special)
        

    if length == len(uppercase):
        return True
    elif string == "":
        return True
    else: return False