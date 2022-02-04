def tupel():
    tuple1 = (3,4,5,6,7,8,9,10)
    sum = 0
    index = 0
    while index<len(tuple1):
        sum = sum + tuple1[index]
        index = index+1
    print(sum)
tupel()