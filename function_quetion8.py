def add_number(num1,num2):
    i=0
    a=[]
    while i<len(num1):
        add=num1[i]+num2[i]
        a.append(add)
        i=i+1
    print(a)
num1=[50,60,10]
num2=[10,20,13]
add_number(num1,num2)