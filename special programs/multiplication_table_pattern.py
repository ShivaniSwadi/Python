# Write a program to print the multiplication table pattern as shown:
# 1 
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

n =  int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i*j, end=' ')
    print('')