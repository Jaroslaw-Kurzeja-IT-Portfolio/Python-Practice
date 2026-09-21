import random
import string

password = "".join([random.choice(string.ascii_letters) for _ in range(10)])
print(password)

print()

password2 = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(20)])
print(password2)
