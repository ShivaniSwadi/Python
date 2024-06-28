# Write a program to print the full pyramid of stars as shown:
# ____*____
# ___*_*___
# __*_*_*__
# _*_*_*_*_
# *_*_*_*_*

# number of whitespaces before the first star = number of rows- row number

Row= int(input("Enter the numner of rows: "))

for i in range(1, Row+1):
    for j in range(1, Row-i+1):
        print(end=' ')
    [print("*", end=' ') for _ in range(1, i+1)]
    print('')


