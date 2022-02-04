def function_name(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    elif len(a)==len(b):
        print(a,b)
a=input("enter a name")
b=input("enter a name")
function_name(a,b)