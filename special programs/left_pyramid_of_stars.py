# Write a program to print the left pyramid of stars as shown:
#         *
#       * *
#     * * *
#   * * * *
# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *


rows = int( input("Enter the numbers of rows: "))

# Upper part of the pyramid
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * i)
    # Lower part of the pyramid
for i in range(rows - 1, 0, -1):
    print("  " * (rows - i) + "* " * i)