def perfect(number):
    s=0
    i=1
    while i<number:
        if number%i==0:
            s=s+i
        i=i+1
    if number==s:
        print(number,"number is perfect number")
    else:
        print(number,"number in not perfect number")
number=int(input("enter a number"))
perfect(number)
