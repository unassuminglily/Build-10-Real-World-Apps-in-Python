# List operations
# codng exercise 1 Append Item to list
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

# Coding Exercise 2 remove item from list
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(seconds[1])
print(seconds)

# fix this with a loop. Exercise 3-- remove three items
second = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
second.remove(second[1])
second.remove(second[1])
second.remove(second[1])
print(second)

#Coding exercise 4 -- Access Item, complete the script so that it prints out the 3rd item of the list serials
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

#Coding exercise 5, complete the script so that it prints out the 1st, 3rd and 6th items of the luts
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

#Coding exercise 6, access and append. Append the first item of weekend to workdays
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])


#Accessing List Slices
monday_temperature = [9.1,8.8, 7.5]
monday_temperature[1:3]
#the upper limit is never included in a python slice
mon_temps = ['hello', 1, 2, 3]
mystring = 'hello'
mystring[1]
mystring[3]
mystring[-3]

#Coding exercise 7; Slicing a list, 2nd to 4th
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

#Coding exercise 8: Slicing a list, first three
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

#Coding exercise 9: Slicing a list, last 3
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])

#Coding Exercise 10:

#DICTIONARIES
""" A dictionary is made of pairs of keys and values. For example, the first pair is "google": 1000000000 where "google" is the key and 1000000000 is the value of that key. """

#Accessing items in dictionaries
student_grades = {"Mary": 9.1, "Sim": 8.8, "lily": 10.0, "John": 7.5}
student_grades("lily")

#"Converting b/n datatypes"
""" 
From tuple to list:

>>> data = (1, 2, 3)
>>> list(data)
[1, 2, 3]
From list to tuple:

>>> data = [1, 2, 3]
>>> tuple(data)
(1, 2, 3)
From list to dictionary:

>>> data = [["name", "John"], ["surname", "smith"]]
>>> dict(data)
{'name': 'John', 'surname': 'smith'}
Note that the original data type needs to have the data structured in a way that can be understood by the new data type.

"""

#CHEATSHEET Operations w Data

"""
In this section, you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4      -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'

"""
