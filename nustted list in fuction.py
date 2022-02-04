def list(list1):
    i=0
    a=[]
    while i<len(list1):
        j=0
        while j<len(list1[i]):
            k=0
            while k<len(list1[i][j]):
                m=0
                while m<len(list1[i][j][k]):
                    n=0
                    while n<len(list1[i][j][k][m]):
                        a.append(list1[i][j][k][m][n])
                        n+=1
                    m+=1
                k+=1
            j+=1
        i+=1        
    print(a)
list1=[[[[[1,2,3],[4,5,6]]]]]
list(list1)
# def list(*list1):
#     i=0
#     a=[]
#     while i<len(list1):
#         a.append(list1)
#         i=i+1
#         print(a)
# list([[[[[[1,2,3],[4,5,6]]]]]])

