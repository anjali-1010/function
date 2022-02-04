num=27
num_digit=list(str(num))
def  harshad_number(num_digit):
    sum=0
    n=num_digit
    while num_digit>0:
        rem=num_digit%10
        sum=sum+rem
        num_digit=num_digit//10
    if (n%sum==0):
        print("true it is a harshad number")
    else:
        print("false it is not harshad number")
harshad_number(int(num))

