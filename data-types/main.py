from modules import helper

# Number
print("Print minutes in 20 days")
print(20 * 24 * 60)

# Strings concatenation
print("20 days are " + str(20 * 24 * 60) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes. But this work only for python > 3.6")
print(f"35 days are {35 * 24 * 60} minutes. But this work only for python > 3.6")
print(f"35 days are {35 * 24 * 60 * 60} seconds. But this work only for python > 3.6")

# Variables
# Global variable
to_seconds = 24 * 60 * 60
to_minutes = 24 * 60
to_hours = 24
name_of_unit = "seconds"
print(f"35 days are {35 * to_seconds} {name_of_unit}.")
print(f"35 days are {35 * to_minutes} minutes.")


# Functions
def days_to_units():
    print(f"110 days are {110 * to_minutes} minutes.")
    print("Ok.")


days_to_units()


# return values from function
def days_to_units_2(days):
    return f"{days} are {days * to_seconds} seconds."


# Functions parameters
def days_to_units_with_parameters(days):
    print(f"{days} days are {days * to_minutes} minutes.")
    print("Ok.")


days_to_units_with_parameters(200)


# Functions default parameters
def days_to_units_with_default_parameters(days=10):
    print(f"{days} days are {days * to_minutes} minutes.")
    print("Ok.")


days_to_units_with_default_parameters()


# Variables scope: local variable, inside a function
def scope_check():
    days: int = 20
    print(name_of_unit)
    print(days)


scope_check()


# Conditional and boolean
def validate_days_to_units(days):
    days_to_int = int(days)
    # validate input
    if days.isdigit():
        result = days_to_units_2(days_to_int)
        print(result)
        # result = days_to_units(nbr_of_days)
        # print(result)
        # days_to_units_with_parameters(nbr_of_days)
    else:
        print("You entered an invalid days")


# Error handling with Try-Except
def validate_with_try_except(days):
    try:
        if days.isdigit():
            print(days_to_units_2(int(days)))
    except ValueError as err:
        print("You entered an invalid days")
        print(str(err))


# User inputs and string casting
# nbr_of_days = input("Enter a number of days to convert in seconds!\n")
# print("You entered " + str(nbr_of_days))
# validate_days_to_units(nbr_of_days)

# While loop
nbr_of_days = ""
while nbr_of_days != "exit":
    nbr_of_days = input("Enter a number of days to convert in hours! Enter 'exit' to close.\n")
    validate_with_try_except(nbr_of_days)

# Lists and For loop
my_list = ["Jan", "Feb", "March", "Jan", "JAN", "feb"]
print(my_list)
print(my_list[1])
my_list.append("April")
print(my_list)
my_list.pop()
print(my_list)
my_list.remove("Jan")
print(my_list)

days_range = ""
while days_range != "exit":
    days_range = input("Enter a sequence of days as comma separated to convert in seconds! Enter 'exit' to close.\n")
    print(type(days_range.split(",")))
    for day in days_range.split(","):
        validate_with_try_except(day)

# Sets
my_set = set(my_list)
my_set_2 = {1, 2, "cat"}
my_set_3 = {"1", 3, 6}
print(my_set)
my_set.add("JANuary")
union_set = my_set.union(my_set_2)
print(union_set)
print(union_set.union(my_set_3))
my_set.clear()
print(my_set)


def validate_and_execute(days, unit):
    try:
        if days.isdigit():
            result = helper.days_to_units(int(days), unit)
            print(result)
    except ValueError:
        print("Invalid input!")


# Dictionary
days_enter = input(helper.input_message)
days_and_unit = days_enter.split(":")
days_and_unit_dic = {"days": days_and_unit[0], "unit": days_and_unit[1]}
print(type(days_and_unit_dic))
print(days_and_unit_dic)
print(validate_and_execute(days_and_unit_dic["days"], days_and_unit_dic["unit"]))

my_dictionary = {
    "days": 20,
    "unit": "hours"
}