def check_number(num1,num2):
    if num1%2==0 and num2%2==0:
        print("dono even hai")
    else:
        print("dono even nahi hai")
check_number(4,3)

def check_number_list(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
           print("even hai")
        else:
            print("even nahi hai")
        i=i+1
list1=[2,6,18,10,3,75]
list2=[6,19,24,12,3,87]
check_number_list(list1,list2)



