

def distance(kms):
    if kms <20:
        print("close")
    elif kms < 50:
        print("median")
    else:
        print("far")
kms=int(input("enter a number"))
distance(kms)