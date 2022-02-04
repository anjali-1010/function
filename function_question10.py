def calculater (num_x,num_y,oprater):
    if oprater=="+":
        add=num_x+num_y
        return add
    elif oprater=="-":
        sub=num_x-num_y
        return sub
    elif oprater=="*":
        multiple=num_x*num_y
        return multiple
    elif oprater=="/":
        division=num_x/num_y
        return division
num_x=int(input("enter num1"))
num_y=int(input("enter num2"))
oprater=input("enter operator")
print(calculater(num_x,num_y,oprater))



