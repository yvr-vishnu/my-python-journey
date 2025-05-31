calculation_of_numbers = 24 * 60 * 60
name_of_units = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days have {calculation_of_numbers} {name_of_units}"

user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print (calculated_value)








