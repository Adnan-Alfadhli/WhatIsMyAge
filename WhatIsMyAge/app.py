from datetime import datetime

year = datetime.today().year

dateOfBirth = input('What is your date birth? ')
age = year - int(dateOfBirth)
msg = f'Your age is {age}'
print(msg)