# def list():
#     i=0
#     a=[]
#     b=[]
#     while i<=10:
#         if i%2==0:
#             a.append(i)
#         else:
#             b.append(i)
#         i=i+1
#     print(a)
#     print(b)
# list()
def fun():
    user=int(input("enter a length"))
    i=0
    a=[]
    b=[]
    while i<=user:
        list1=int(input("enter a number"))
        list2=int(input("enter a number"))
        a.append(list1)
        b.append(list2)
        j=0
        c=[]
        while j<=i:
            c.append(a[j]+b[j])
            j=j+1
        i=i+1
    print(c)
fun()