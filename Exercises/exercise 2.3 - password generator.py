import random

minimum_length = random.randint(8, 20)
n_lowercase = 2
n_uppercase = 2
n_numbers = 2
n_special = 2
n_extra = max([0, minimum_length - n_lowercase - n_uppercase - n_numbers - n_special])

# import string
# LOWERCASE_CHARACTERS = string.ascii_uppercase
# UPPERCASE_CHARACTERS = string.ascii_lowercase
# NUMBER_CHARACTERS = string.digits
# SPECIAL_CHARACTERS = string.punctuation
#or

LOWERCASE_CHARACTERS = 'abcdefghijkmnopqrstuvwxyz'  # removed l
UPPERCASE_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # removed I and O
NUMBER_CHARACTERS = '0123456789'
SPECIAL_CHARACTERS = '@#$%&*+?!{}'

ALL_CHARACTERS = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + NUMBER_CHARACTERS + SPECIAL_CHARACTERS

lowercase = random.choices(LOWERCASE_CHARACTERS, k = n_lowercase)
uppercase = random.choices(UPPERCASE_CHARACTERS, k = n_uppercase)
numbers = random.choices(NUMBER_CHARACTERS, k = n_numbers)
special = random.choices(SPECIAL_CHARACTERS, k = n_special)
extra = random.choices(ALL_CHARACTERS, k = n_extra)

all_characters = lowercase + uppercase + numbers + special + extra

random.shuffle(all_characters)

password = ''.join(all_characters)

print('New password: ', password)
