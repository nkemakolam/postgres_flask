import random

def main():
    # ask user for number
    user_number = get_player_number()
    # CALCULATE THE LOTERY NUMBER
    lottery_value = create_lottery_numbers()
    # PRINT WINNER
    match_number = user_number.intersection(lottery_value)
    print("you match {}. You won ${}".format(match_number, 100 ** len(match_number)))

# user can pick 6 number
def get_player_number():
    number_csv= raw_input("Enter 6 number , separated by comma: ")
    # now i want to create a set of integer from the the number_csv
    numner_list = number_csv.split(",") #['1','2,'...']
    integer_set = {int(number) for number in numner_list}
    return integer_set

# lotery calculate 6 random (between 1 and 20)

def create_lottery_numbers():
    lottery_value = set()
    while len(lottery_value)< 6:
        lottery_value.add(random.randint(1, 20))
    return lottery_value

main()
# then we match the user number to the lottery number
# Calculate the winning base on the how many the user matched

# print("running the second fucntion")
# print(create_lottery_numbers())
# print("################################")
# print(get_player_number())