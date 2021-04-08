# Split value is essential when you require user to give us various value at same time
#Every string has a method called split tat allows us generate a list from a string
# demo
# split methode does not work on input function in version 3 instead use raw_input(),it only works on version 2 use input()
# ref https://stackoverflow.com/questions/33292492/attributeerror-tuple-object-has-no-attribute-split-with-result-of-input


lottery_num = raw_input("Enter your number separated by commas: ")
result=lottery_num.split(",")
print(result)


user_numeber_as_integer=[]
for number in result:
    user_numeber_as_integer.append(int(number))
print(user_numeber_as_integer)

print([int(num) for num in result]) # Here we using list comprehensionm


print("runing logic to")
## using for each and list comprehension
user_number='12345'
user_number_as_int=[]
for number in user_number:
    user_number_as_int.append(int(number))

print(user_number_as_int)

print([num for num in user_number_as_int]) # list comprehension implementation


