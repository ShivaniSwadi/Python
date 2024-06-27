# lets consider a list of fruits that includes four types of fruits: apple, baanana, mango and strawberry.
# write a program to determine whether the fruit orange is present in the list.

fruits = ['apple', 'banana', 'mango', 'strawberry']
fruits_len = len(fruits)
index = 0

while index < fruits_len:
    if fruits[index] == 'orange':
        print(" Orange is Available!!")
        break
    index += 1

else:
    print("Orange is not Available!!")   

