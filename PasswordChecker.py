import string

password = "helloWorld"

upper_case = any(char in string.ascii_uppercase for char in password)
lower_case = any(char in string.ascii_lowercase for char in password)
special_case = any(char in string.punctuation for char in password)
digits = any(char in string.digits for char in password)

characters = [upper_case, lower_case, special_case, digits]

length = len(password)

#file that contain common passwords
with open('10k most common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in common list! Score: 0 / 7")

score = 0

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 25:
    score += 1

print(f"Password length is {length}, adding {score} points!")

num_character_types = sum(characters)

if num_character_types > 1:
    score += num_character_types - 1

print(f"Password has {num_character_types} different character types, adding {num_character_types - 1} point(s)!")


if score < 4:
    print(f"The password is quite weak! Score: {score} / 7")
elif score == 4:
    print(f"The password is ok! but not that good, Score: {score} / 7")
elif 4 <= score < 6:
    print(f"The password is good! Score: {score} / 7")
else:
    print(f"The password is strong! Score: {score} / 7")