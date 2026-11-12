from datetime import datetime

# ---------------------------------------------------------
# Requirement 1: Store first name in a variable (all lowercase)
# ---------------------------------------------------------
first_name = "muneeb"

# ---------------------------------------------------------
# Requirement 2: Store last name in a variable (all uppercase)
# ---------------------------------------------------------
last_name = "HASSAN"

# ---------------------------------------------------------
# Requirement 3: Print greeting - first name uppercase, last name lowercase
# (using the upper() and lower() string functions)
# ---------------------------------------------------------
print("Hello, " + first_name.upper() + " " + last_name.lower())

# ---------------------------------------------------------
# Requirement 4: Print out two newlines
# (the "\n" in the string plus the newline print() adds = two newlines)
# ---------------------------------------------------------
print("\n")

# ---------------------------------------------------------
# Requirement 5: Print the quote with quotation marks at the start and end
# ---------------------------------------------------------
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# ---------------------------------------------------------
# Requirement 6: Store 2 decimal numbers as variables
# ---------------------------------------------------------
num1 = 8.5
num2 = 2.5

# ---------------------------------------------------------
# Requirement 7: Store one addition, subtraction, multiplication,
# and division of those variables as variables
# ---------------------------------------------------------
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# ---------------------------------------------------------
# Requirement 8: Print each of the four results on its own line
# ---------------------------------------------------------
print()  # blank line to separate from the quote
print(str(num1) + " plus " + str(num2) + " equals " + str(addition))
print(str(num1) + " minus " + str(num2) + " equals " + str(subtraction))
print(str(num1) + " times " + str(num2) + " equals " + str(multiplication))
print(str(num1) + " divided by " + str(num2) + " equals " + str(division))

# ---------------------------------------------------------
# Requirement 9: Store the current month (string) and day of month (number)
# ---------------------------------------------------------
today = datetime.now()
month = today.strftime("%B")   # month name as a string, e.g. "November"
day = today.day                # day of the month as a number, e.g. 9

# ---------------------------------------------------------
# Requirement 10: Print on a new line, tabbed over two times
# ---------------------------------------------------------
print("\n\t\tToday is day " + str(day) + " of the month of " + month + ".")
