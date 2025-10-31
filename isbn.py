def is_valid(isbn):
    alphabet="abcdefghijklmnopqrstuvwyz"
    alphabetx="abcdefghijklmnopqrstuvwxyz"
    isbn_clean= isbn.replace("-","")
    total=0
    number=list(isbn_clean)
    if len(number) !=10:
        return False
    for char in number:
        if char.lower() in alphabet:
            return False
    for i in range(10):
        if number[i]== "X": 
            number[i]=10
            total= total+ 10*1
        else:
            digit = int(number[i])
            added= digit*(10-i)
            total=total+added
    return total%11==0
    