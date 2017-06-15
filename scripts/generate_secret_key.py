import string
import random

SECRET_KEY = string.ascii_letters+string.digits+string.punctuation
print repr(''.join([random.SystemRandom().choice(SECRET_KEY) for i in range(random.randint(45, 50))]))
