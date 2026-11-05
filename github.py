# Logical operators
# and (and) or (or) not (not)
# and - All conditions must be
# True.
# If any value is considered False,
# the entire expression will be evaluated to that value.
# The following values are considered falsy (which you have already seen):
# 0 0.0 '' False
# There is also the None type, which is
# used to represent a no-value.


choice = input('Do you want a Peanut Candy or a pizza? ')
print('Hint: I love it')
entered_password = input('Password: ')

allowed_password = 'i_love_peanut_candy'

if choice == 'Peanut Candy' or choice == 'peanut candy' and entered_password == allowed_password:
    print('Fresh peanut candy is awesome!')
else:
    print('You did not enter anything.')


# Logical operators
# and (and) or (or) not (not)
# or - Any True condition evaluates
# the entire expression as True.
# If any value is considered True,
# the entire expression will be evaluated to that value.
# The following values are considered falsy:
# 0 0.0 '' False
# There is also the None type, which is
# used to represent a no-value.

# choice = input('[E]nter [S]top: ')
# entered_password = input('Password: ')

# allowed_password = '123456'

# if (choice == 'E' or choice == 'e') and entered_password == allowed_password:
#     print('Enter')
# else:
#     print('Exit')

# Short-circuit evaluation
# password = input('Password: ') or 'No password'
# print(password)

#Logical operator "not"
#Used to reverse expressions.
#not True = False
#not False = True

'''
password = input('Password: ')

if password == 'i_love_peanut_candy':
    print('Peanut candy is really good!')
else:
    print('Incorrect password.')
print(not False)
'''
# Operators in and not in
# Strings are iterable
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# name = 'Otávio'
# print(name[2])
# print(name[-4])
# print('vio' in name)
# print('zero' in name)
# print(10 * '-')
# print('vio' not in name)
# print('zero' not in name)
'''
name = input('Enter your name: ')
find = input('Enter what you want to find: ')

if find in name:
    print(f'{find} is in {name}')
else:
    print(f'{find} is not in {name}')
'''