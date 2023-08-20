from werkzeug.security import generate_password_hash, check_password_hash

password = 'mysecretpassword'
hashed_pass = generate_password_hash(password=password)

print(hashed_pass)

check1 = check_password_hash(hashed_pass, 'wrongpassword')
check2 = check_password_hash(hashed_pass, 'mysecretpassword')

print(check1) # False
print(check2) # True