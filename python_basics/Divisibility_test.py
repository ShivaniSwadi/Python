#Whether a number divisible by 2 or 3

n= int(input("Enter the number: "))
if n % 2 == 0:
    print("The number is divisible by 2")
elif n % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is neither divisible by 2 nor by 3")

print("DONE!")