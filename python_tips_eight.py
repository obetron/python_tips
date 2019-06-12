
#wrong way to get a secret info from user
username = input('Username:')
password = input('Password:')

print('logging in...')
print('Username: ', username)
print('Password: ', password)
"""
OUTPUT:
Username:Eren
Password:1234 #password seeing from anyone
logging in...
Username:  Eren
Password:  1234
"""

#right way to get sercret infor from user
from getpass import getpass

username1 = input('Username:')
password1 = getpass('Password:')

print('logging in...')
print('Username1: ', username1)
print('Password1: ', password1)
