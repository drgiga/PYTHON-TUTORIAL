#  Catching exceptions using try and except

user_input = input("Please Enter You Age:")
try:
    user_input = int(user_input) # ValueError: invalid literal for int() with base 10: 'davoud'
    print("Your Age is: ",user_input)
except:
    print("Error Occured -> Because you have entered a non-numeric. ",type(user_input))


