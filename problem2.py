#! python3
"""
Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list

inputs:
string

outputs:
list

examples:
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:kiwi
['apple', 'cherry', 'apple', 'banana', 'strawberry', 'blueberry']

['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:orange
word not in list
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi', 'orange']

"""

fruit = ["apple","cherry","kiwi","apple","banana","strawberry","kiwi","blueberry","kiwi","tomato"]
print(fruit)
word = input("Enter a word from the list: ")

num = fruit.count(word)

if word not in fruit:
    print("word not in list")
    
for x in range(num):
    if word in fruit:
        fruit.remove(word)

print(fruit)