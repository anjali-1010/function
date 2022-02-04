def calculate(num_x,num_y):
    # num_x=[5,10,50,20]
    # num_y=[2,20,3,50
    i=0
    a=[]
    while i<len(num_x):
        multiple=num_x[i]*num_y[i]
        a.append(multiple)
        i=i+1
    print(a)
calculate([5,10,50,20],[2,20,3,50])




