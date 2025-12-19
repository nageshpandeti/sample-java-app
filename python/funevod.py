x=int(input("please enter a number"))

def evenodd(x):
    if x == 0:
        print("zero Number is entered")
    elif x % 2 == 0:
        print("even Number is entered")
    else:
       print("Entered number is odd")

evenodd(x)