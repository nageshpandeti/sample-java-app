x = int(input("Please enter number: "))

def square(x):
    if x <= 5:
        return x * x   

print(square(x))

square=[x**2 for i in range(1,5)]
print(square)


