import random

def ask_user_and_check_number():
    user_number = int(input("Enter Enter your lucky number: "))
    if user_number in magic_number:
        return "You got the number right !"
    if user_number not in magic_number:
        return "You didnt get it right!"

magic_number = [random.randint(0,9), random.randint(0,9)]


def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is attempt {}".format(attempt))
        message = ask_user_and_check_number()
        print(message)

user_attempt = int(input("Enter number of attempt: "))
run_program_x_times(user_attempt)