# ---------------------------------------------------------
# Requirement 1: Create a list of courses taken at Walsh College
# (each course stored in all lowercase letters)
# ---------------------------------------------------------
courses_taken = ["mth300", "mgt201", "qm202", "it405", "it408", "com405", "ecn201", "it402", "ecn202"]

# ---------------------------------------------------------
# Requirement 2: Sort the list and print each element with a message
# (course printed in all uppercase letters)
# ---------------------------------------------------------
courses_taken.sort()
course_list = courses_taken[:]   # working copy so courses_taken stays unchanged until requirement 11
for course in course_list:
    print("I have taken " + course.upper() + " at Walsh College.")

# ---------------------------------------------------------
# Requirement 3: Add upcoming courses, re-sort, and print the list
# ---------------------------------------------------------
# Courses I plan to take next term (change these to match your real plan)
course_list.append("it410")
course_list.append("com410")
course_list.append("mgt301")
course_list.sort()

print()
print("This is my course of study with upcoming courses added:")
for course in course_list:
    print(course)

# ---------------------------------------------------------
# Requirement 4: Remove every course I've already taken from the list
# and print each removed course
# ---------------------------------------------------------
print()
print("I do not have to take these courses:")
for course in courses_taken:
    course_list.remove(course)
    print(course)

# ---------------------------------------------------------
# Requirement 5: Print the courses left in the list, each on its own line
# ---------------------------------------------------------
print()
print("I plan to take the following courses next term")
for course in course_list:
    print(course)

# ---------------------------------------------------------
# Requirement 6: Create a list of numbers from 1 to 1000 divisible by 6
# ---------------------------------------------------------
numbers = list(range(6, 1001, 6))   # starts at 6, steps by 6, stops at or below 1000

# ---------------------------------------------------------
# Requirement 7: Print the first 20 numbers, each on its own line
# ---------------------------------------------------------
print()
print("Here are twenty numbers divisible by 6.")
for number in numbers[:20]:
    print(number)

# ---------------------------------------------------------
# Requirement 8: Calculate the maximum number in the original large list
# ---------------------------------------------------------
max_number = max(numbers)

# ---------------------------------------------------------
# Requirement 9: Print the maximum value with the message
# ---------------------------------------------------------
print()
print("The maximum value in the list is: " + str(max_number))

# ---------------------------------------------------------
# Requirement 10: Sum the values between the 10th and 50th values
# (inclusive) and print the sum with the message
# ---------------------------------------------------------
# 10th value is at index 9 and 50th value is at index 49, so the slice ends at 50
sum_of_values = sum(numbers[9:50])
print("Here is the sum of several values in the list: " + str(sum_of_values))

# ---------------------------------------------------------
# Requirement 11: Overwrite the original courses-taken variable
# with the large list of numbers
# ---------------------------------------------------------
courses_taken = numbers
