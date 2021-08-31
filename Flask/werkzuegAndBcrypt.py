from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

password = "rajani"

bcrypt = Bcrypt()

hashed_password = bcrypt.generate_password_hash(password=password)
hashed_password_wer = generate_password_hash(password)

print(hashed_password)
print(hashed_password_wer)

check = bcrypt.check_password_hash(hashed_password, 'rajani')
print(check)
check_wer = check_password_hash(hashed_password_wer, 'rajni')
print(check_wer)
