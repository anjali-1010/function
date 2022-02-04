# def add(num1,num2):
#     return add (num1,num2)
# print(add(2,3))
# def one_to_ten(num):
#     if(num==1):
#         print (one_to_ten)
#     return one_to_ten(num-1)
# print(one_to_ten(5))
def one_to_ten(num):
    if (num==1):
        print(num) 
    c=one_to_ten(num-1)
    return c
print(one_to_ten(5))


