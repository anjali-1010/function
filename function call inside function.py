def sum():
    i=0
    s=0
    while i<student:
        number=int(input("enter a student number"))
        s=s+number
        i=i+1
    return s

student=int(input("enter a number"))
call = sum()
print(call)

def avg():
    avg1=call/student
    print(avg1)

avg()




