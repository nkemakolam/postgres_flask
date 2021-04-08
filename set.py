winning_number=set()
winning_numbers=set()
lottery_value = {3,4,5,5,6,9}
user_values = {2,9,4,10}
winning_number = lottery_value.intersection(user_values)
winning_numbers = lottery_value.union(user_values)
print(winning_number)
print(winning_numbers)
