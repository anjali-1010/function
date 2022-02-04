def eligible_for_vote(age):
    if age>=18:
        print("eligible for voting")
    else:
        print("not eligible for vote")
a=int(input("enter a age"))
eligible_for_vote(a)