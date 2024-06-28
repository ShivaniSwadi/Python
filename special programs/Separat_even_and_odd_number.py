# write a program to separate even and odd numbers stored in a list into two different lists

#num_list=list(range(1, 25))
num_list= [int(n) for n in input("Enter the list of numbers to be separated: ").split()]
even = []
odd = []

for num in num_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)