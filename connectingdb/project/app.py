from database import Database
from user import User

Database.initialise()
my_user = User ('Raymond@gmail.com','maxwell','josh',None)
print(my_user.save_to_db())

my_user_data = User.load_from_db_by_email('Lizibert@gmail.com')
print(my_user_data)
