............................................
Introduction 
............................................
Why python ??
	Easy to learn  --> simple syntax, easy to setup
	large eco systems ---> 
	Flexible ----> we can extend python

Where Python is used ???
	Web Development
	Data Scence
	ML and AL  - Face recognition
	Web Scraping ----> 
	Mobile develpoment
	Automation  -----> cicd, cloud platforms, backup and clean ups, exel sheets, 
	
............................................
Introduction 
............................................


............................................
Local Setup and install and IDE Setup
............................................

Install in windows and Linux
windows
	Download Python click exe file next next next
Linux
	python --version
	python2.7.10 ---> we dont use this, we wil keep it as it is
	Lets Install Python3
		python3 --version
		sudo apt update
		sudo apt install python3-pip
		Install dependencies as well
		
IDE
	Pycharm is the best IDE tool will provide advanced features

	Download Pycharm -- proffessional version vs community version 
	Professional eddtion we downlaoded from with nana discount code which is free for 3 months
	Once the pycharm downlaoded and installed
	create a new project
	
............................................
Local Setup and install and IDE Setup
............................................


............................................
Demo-1 Write your 1st script to print anything
............................................
print numbers
	print(1)
		output 1
	print(100+200)
		output 300
	print(1.1)
		output 1.1
print text
	print("100 is a number")
		output 100 is a number

............................................
Demo-1 Write your 1st script to print anything
............................................


............................................
Demo-2 string and Numbers 
............................................

Data Types	
	Strings(str)  -- single quotes and double quotes are same
	Numbers 
		integer(int) --> whole nubers like 1,2,3
		float(flt) --> 1.1
Now lets get into some use cases 
	calculator
		How many minutes are there in 20 days ???
			60*24 = 1440
			1440*20 = 28800
		print(20 * 24 * 60)
............................................
Demo-2 string and Numbers 
............................................


............................................
Demo-3 string cocatenation
............................................
How do we get the minutes caluclated vlaue in 2nd line in 1s line ????
	print("20 days have xxx minutes")
	print(20 * 24 * 60)
	
In general + sybol is used to add any stings in coding laguage
print("20 days have" + (20 * 28 * 60) + "minutes")

we get this error 
	TypeError: can only concatenate str (not "int") to str

Sting cacatinatio	
	print("20 days have " + str(20 * 28 * 60) + " minutes")
		output : 20 days have 33600 minutes
		
	
Instead of this str() we use {}
	print("20 days have {20 * 28 * 60} minutes")
		output: 20 days have {20 * 28 * 60} minutes
		

		
Now issue is interprter takes above as sting and does not do caluculation
Inorder to overcome this and get the answer instead of simply printing wu use f which stands for format sting
	print(f"20 days have {20 * 24 * 60} minutes")
		output: 20 days have 28800 minutes
Note: THIS f formate works only after 3.9 python versions does not works for version 2
............................................
Demo-3 string cocatenation
............................................
	
	
................................................................
Demo-4 Variable ( variables are containers for storing values)
.................................................................
Problem:
	print(f"20 days have {20 * 24 * 60} minutes")
	print(f"30 days have {30 * 24 * 60} minutes")
	print(f"40 days have {40 * 24 * 60} minutes")
	print(f"60 days have {60 * 24 * 60} minutes")
	print(f"110 days have {110 * 24 * 60} minutes")
Now we are able to caluculate minutes for above, but requirement has changed 
and we need to calucate seconds then we need to multiply * 60 and also need to change minutes as seconds
This is repetative and we need to edit this for all 5 lines
		print(f"20 days have {20 * 24 * 60 * 60} seconds")
		print(f"30 days have {30 * 24 * 60 * 60} seconds")
		print(f"40 days have {40 * 24 * 60 * 60} seconds")
		print(f"60 days have {60 * 24 * 60 * 60} seconds")
		print(f"110 days have {110 * 24 * 60 * 60} seconds")

how do we overcome this ????

Solution:
	calculation_to_units = 20 * 24 * 60  
	name_of_unit = "seconds"
	print(f"20 days have {20 * calculation_to_units} {name_of_unit}")
	print(f"30 days have {20 * calculation_to_units} {name_of_unit}")
	print(f"40 days have {20 * calculation_to_units} {name_of_unit}")
	print(f"60 days have {20 * calculation_to_units} {name_of_unit}")
	print(f"110 days have {20 * calculation_to_units} {name_of_unit}")
	
Note: Use descriptive varibles names so other programmers also understands what the value is

................................................................
Demo-4 Variable ( variables are containers for storing values)
.................................................................

.........................................................................................
Demo-5 Functions ( To avoid repeating the same logic or block of code we use funtions )
.........................................................................................
Problem:
	With above exmple is duplication of lines, how do we avoid duplication of lines
	we can achive this using Functions
	
Solution:
	syntax:
		def days_to_untis():	
			print(f"20 days have {20 * calculation_to_units} {name_of_unit}")
			print("All good!")

	output: Process finished with exit code 0

	see the output for days_to_units funtion, why there is no output
	that is bcz funtion needs to be called but we only defined it now

	Funtions:
		A Funtion is defined using the def keyword
		Block of code which only runs when it is called
		
So we know funtions needs to be used are called but to call the function ????

Just use the funtion name
	days_to_units()
...........................................................
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_units():
    print(f"20 days have {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units()
............................................................

Output: now we can see the actual code which is in function
	20 days have 1728000 seconds
	All good!

	Process finished with exit code 0
	
		
.........................................................................................
Demo-5 Functions ( To avoid repeating the same logic or block of code we use funtions )
.........................................................................................


.........................................................................................
Demo-6 Functions-parameters ( function parameters or arguments used to specify input )
.........................................................................................
def days_to_units():
    print(f"20 days have {20 * calculation_to_units} {name_of_unit}")
    print("All good!")
	
Problem: 
	Now in print statement how to use other values inplace of 20 days have, if i need to specify my own value
	how do we do it
			print(f"20 days have {20 * calculation_to_units} {name_of_unit}")
			print(f"30 days have {20 * calculation_to_units} {name_of_unit}")
			print(f"40 days have {20 * calculation_to_units} {name_of_unit}")
			print(f"60 days have {20 * calculation_to_units} {name_of_unit}")
			print(f"110 days have {20 * calculation_to_units} {name_of_unit}")
	
Solution:
	use concept of funtions parameters 
..........................................................................................
	calculation_of_numbers = 24 * 60 * 60
	name_of_units = "seconds"

	def days_to_seconds(num_of_days, status):
		print(f"{num_of_days} days have {num_of_days * calculation_of_numbers} {name_of_units}")
		print(status)


	days_to_seconds(30, "Awesome")
..........................................................................................

.........................................................................................
Demo-6 Functions-parameters ( function parameters or arguments used to specify input )
.........................................................................................


.........................................................................................
Demo-7 scope of a variable ( global vs local )
.........................................................................................

	Variables defined in the script are global variables, variables which are only defined inside function are local variables
	we cant access local varibles 
	we can only access global variables 
	
Example:
	#Global Variables 
	calculation_of_numbers = 24 * 60 * 60
	name_of_units = "seconds"

	def days_to_seconds(num_of_days, status):
		#num_of_days is local Variables
	
		print(f"{num_of_days} days have {num_of_days * calculation_of_numbers} {name_of_units}")
		print(status)


	days_to_seconds(30, "Awesome")
	
	def scope_check():
		#Valid and accessible
		print(name_of_units)
		
		#InValid and can't be accessible
		print(num_of_days)
		
		
Output:
		  File "C:\Users\Vishnu\PycharmProjects\my-python-project\main.py", line 14, in scope_check
    print(num_of_days)
          ^^^^^^^^^^^
NameError: name 'num_of_days' is not defined

Solution:

def scope_check(num_of_days):
    print(name_of_units)
    print(num_of_days)
scope_check(40)

Note: What ever we can do out side the function we can do same things in inside function as well
i.e. we can define variables inside function

.........................................................................................
Demo-7 scope of a variable ( global vs local )
.........................................................................................


.........................................................................................
Demo-8 User Input -- input() --- which is a built in function in python
.........................................................................................

How to accept user input in python ????
	#This will allow user to provide input
	input()
Build-in-funtion: built in functions are provided by python language itself, there are 1000's of
built-in-functions like this which were written by programmer, whcih can be used by us

	input("Hey user, enter a number of days and I will convert it  to hours!\n")
	
we can defined this as varibles
	
	user_input = input("Hey user, enter a number of days and I will convert it  to hours!\n")
	print(user_input)

.........................................................................................
Demo-8 User Input -- input() --- which is a built in function in python
.........................................................................................	


......................................................................................................
Demo-9 Funtion with Return Values  ( Return values  ( A function can return data as a result )
......................................................................................................
	
	
calculation_of_numbers = 24 * 60 * 60
name_of_units = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days have {calculation_of_numbers} {name_of_units}"

user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print (calculated_value)

Try to save this script as .py file and try to run it, it should give the calculated value

......................................................................................................
Demo-9 Funtion with Return Values  ( Return values  ( A function can return data as a result )
......................................................................................................
		
......................................................................................................
Demo-10 Conditionals (if / else) & Boolean Data type
......................................................................................................
What if user enters nagetive value or text how to handle that in our script ?????
For validating user Input	
	which doesn't make sense
	that could crash our program
	could even be a security risk

	
Conditionals
	Expressions that evaluate to either true or false
		Equal: a==b
		Not Equal: a != b
		Less than: a < b
		Greater than: a > b
		Greater than or equal to: a >= b
		
.........................................................
	def days_into_hrs(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days have {num_of_days * calculation} {num_of_units}"
    else:
        return f"entered value is not a positive number, please enter valid input"
.......................................................................

Boolean value has two values true and false
If condition is met it is true or else it is false

	def days_into_hrs(num_of_days):
		#This makes sure to print true or false
		print(num_of_days > 0)
		if num_of_days >= 0:
			return f"{num_of_days} days have {num_of_days * calculation} {num_of_units}"
		elif no_of_days == 0
			return f"entered number is zero, please enter a valid number"
		else:
			return f"entered value is not a positive number, please enter valid input"

......................................................................................................
Demo-10 Conditionals (if / else) & Boolean Data type
......................................................................................................
	
	
	
......................................................................................................
Demo-11 More user input validations
......................................................................................................

What if user inputs some text instead of a + number how to ahndle it ????

	user_input = input("hey user enter num of days i will provide minutes\n")
	if user_input.isdigit():
		user_input_num = int(user_input)
		calculated_value = days_into_hrs(user_input_num)
		print(calculated_value)
	else:
		print("entered input is not valid, please enter valid + number ")
		
Now my script will handle if the user input is not a +ve number ( non nagative, text, float input errors will be handled)
		
......................................................................................................
Demo-11 More user input validations
......................................................................................................


......................................................................................................
Demo-12  Clean up our script
......................................................................................................

def user_input_validation():
    if user_input.isdigit():
        user_input_num = int(user_input)
        calculated_value = days_into_hrs(user_input_num)
        print(calculated_value)
    else:
        print("enter a valid +ve number")
user_input = input("hey user enter num of days i will provide minutes\n")
user_input_validation()

......................................................................................................
Demo-12  Clean up our script
......................................................................................................


......................................................................................................
Demo-13  Nested if...else
......................................................................................................

	def user_input_validation():
    if user_input.isdigit():
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_into_hrs(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            return f"entered number is zero, please enter a valid +ve number"

    else:
        print("enter a valid +ve number")
......................................................................................................
Demo-13  Nested if...else
......................................................................................................


......................................................................................................
Demo-14 Error handling Try/Except
......................................................................................................

The try block: lets you test a block of code for errors
The except block: Catches the error and lets you handle it

def user_input_validation():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_into_hrs(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            return f"entered number is zero, please enter a valid +ve number"
        else:
            print("entered number is invalid, please enter a valid +ve number")

    except ValueError:
        print("enter a valid +ve number")

......................................................................................................
Demo-14 Error handling Try/Except
......................................................................................................


......................................................................................................
Demo-15 While loops
......................................................................................................

Looping
	To execute logic multiple times
	Python has 2 loop commands
	
Conditions
	- evaluate to true or false
	- Are used most commonly in "if statements" and "loops"
	
while True:
    user_input = input("hey user enter num of days i will provide minutes\n")
    user_input_validation() 
	
Now user enters any input conditons execues if it is true, and program does not crash if the value is non +ve 
instead it will ask use agin to ener input

Output:
hey user enter num of days i will provide minutes
50
50 days have 72000 minutes
hey user enter num of days i will provide minutes

......................................................................................................
Demo-15 While loops
......................................................................................................


......................................................................................................
Demo-15 Lets user exit the program
......................................................................................................
With this change if user enters exit program exits

#If we dont define first line while loop fails with user_input not defined error
user_iput = ""
while user_input != "exit":
    user_input = input("hey user enter num of days i will provide minutes\n")
    user_input_validation() 

Output:
20
20 days have 28800 minutes
hey user enter num of days i will provide minutes
exit
enter a valid +ve number

Process finished with exit code 0

......................................................................................................
Demo-15 Lets user exit the program
......................................................................................................


......................................................................................................
Demo-16 Lists and for loops
......................................................................................................

Data types we discussed so far are

- string - any text in double quotes "test"
- Float  - fraction numbers  like 1.1
- Integer  - whole numbers
- Boolean  - true or false

List is an other data type To store multiple items in a single variable
In our case we need to provide list of whole numbers 
But list allow us to provide any datatype like group of stings or group of floating bumbers or list of boolean
[10, 15, 40, 100, 200]

Requirement here is for each value in the user list we want to execute user_input_validation() funtion
How do we achive that ???? 

we can achive that using For loops

For Loop:
	- is used for iterating over a sequence (like a list)
	- So we can execute this for each item in the list
	
.........................................................

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
    #input is a string that needs to be converted to list, which is done by split() function with ,
    # which means input should be entered like this 10, 30, 60 based , split functon splits the inputs
    for num_of_days_unit in user_input.split(","):
        user_input_validation()

.........................................................

......................................................................................................
Demo-16 Lists and for loops
......................................................................................................