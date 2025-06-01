#convert days into hours
#n days * 24 hrs
calculation =  24 * 60
num_of_units = "minutes"


def days_into_hrs(num_of_days):
        return f"{num_of_days} days have {num_of_days * calculation} {num_of_units}"

def user_input_validation():
    try:
        user_input_num = int(num_of_days_unit)
        if user_input_num > 0:
            calculated_value = days_into_hrs(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            return f"entered number is zero, please enter a valid +ve number"
        else:
            print("entered number is invalid, please enter a valid +ve number")

    except ValueError:
        print("enter a valid +ve number")

user_input = ""
while user_input != "exit":
    user_input = input("hey user enter num of days as comma separated list i will convert days to minutes\n")
    print(type(user_input.split()))
    print(user_input.split(", "))
    #input is a string that needs to be converted to list, which is done by split() function with ,
    # which means input should be entered like this 10, 30, 60 based , split functon splits the inputs
    for num_of_days_unit in user_input.split(", "):
        user_input_validation()