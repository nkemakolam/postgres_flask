from user import User
my_user = User ('Lizibert@gmail.com','maxwell','josh',None)
print(my_user.save_to_db())

my_user_data = User.load_from_db_by_email('nkem@gmail.com')
print(my_user_data)
