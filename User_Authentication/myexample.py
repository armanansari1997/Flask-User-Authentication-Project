from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'mysecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)

# print(hashed_password)

check1 = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
check2 = bcrypt.check_password_hash(hashed_password, 'mysecretpassword')
print(check1) # False
print(check2) # True
