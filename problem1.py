#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
nameList = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(nameList)
remove_name = input("Choose a person from the list to replace: ")

num = nameList.index(remove_name)
num = int(num)
nameList.remove(remove_name)

add_name = input("Enter the replacement: ")

nameList.insert(num, add_name)
print(nameList)