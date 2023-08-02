import random
import string


def creat_unique_id():
    # Generate a random string
    # with 32 characters.
    random_id = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_id
