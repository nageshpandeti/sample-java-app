str1="hello"
str2="word"

str3= str1 + " " +str2
print(str3)

length=len(str3)
print(length)


length=len(str3)
print(length)

uppercase=str1.upper()
print (uppercase)

lowercase=str1.lower()
print (lowercase)

rep=" nagesh hemanth   "

result=rep.replace('hemanth','lakshmi')
print(result)

rep1="harry potter"
result1=rep1.split()
print(result1) 


text = "  Python is awesome   "
words = text.split()
print("Words:", words)

resource=text.strip()
print(resource)

substring="it"

if substring in text:
    print("it is available") 
else: 
   print("it is not availbale")

# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

