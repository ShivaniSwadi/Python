# write a program to print the sandglaa pattern of stars as shown:
# * * * * *
#  * * * *
#   * * * 
#    * * 
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


row = int(input("Enter the number of rows: "))
for i in range(1,row+1):
    print(' '*(i)+ '* '*(row+1-i))

for i in reversed(range(1, row+1)):
    print(' '*(i)+ '* '*(row+1-i))