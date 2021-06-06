#Coding Exercise 1
#Creating integers, strings & floats
mood = "good"
strength = 7.0
rank = 3

#Coding exercise 2
#Summing numbers
x = 6
y = 5 
z= 4
s = x+y+z
print(s)

#Lists are a form of compound data type because they're made up of different data types
stud_grades = [7, 8, 9, 10]
print(stud_grades)
#Can create a list of numbers autmo using a range
print(list(range(1,17,2)))

#Coding Exercise 3
#Create a lits
temperatures = [34.5, 7, "dog?"]

#Coding Exercise 4
#Create a complex list
rainfall = [33.3, 3, "humid", ["amazon", "bog", 1]]

#Look at the data types by exploring them with the dir command

mysum = sum(stud_grades)
length = len(stud_grades)
mean = mysum/length
print(mean)

#Coding Exercise 5 Calculate Maximum
student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)

#Coding Exercise 6 Count Values
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
ct = student_grades.count(10.0)
print(ct)

#Coding Exercise 7 Modify String
username = "Python3"
print(username.lower())

#DICTIONARIES
stud_grades = {"Harry": 9.1, "Louis": 8.8, "Niall": 10.0, "Zayn": 7.7 }

#Coding Exercise 8 Create Disctionary
day_temperatures = {"morning": 27.8, "noon": 33.9, "evening": 30.2}

#TUPLES
#Like a list with paranthesis, tuples are immutable meaning they can't be changed or added. Faster than lists.
tupperware = (8, 9, 10, "baby", "here boy", "castaways")

#  Coding Exercise 9 Create Tuples
color_codes = ((9,2), (3,0), ("lilsss", 8))

# Coding Exercise 10 Create Complex Dictionary
#This one has dictionaries and tuples
day_temperatures = {"morning": (26.1, 6.5, 3.3), "noon": (36.9, 4.3, 88.9), "evening": (32.0, 64.4, 6.4)}
