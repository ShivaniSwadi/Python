# Write a program to print the right pyramid of stars as shown:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * 
# * * *
# * *
# *

row = int( input("Enter the numbers of rows: "))

for i in range(1, row+1):
    [print("*", end=' ') for _ in range (1, i+1)]
    print('')

for k in reversed(range(0, row)):
    [print('*', end=' ') for _ in range(1, k+1)]
    print('')