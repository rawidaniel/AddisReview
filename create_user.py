#!/usr/bin/python3
"""Create a new admin user able to view the /reports endpoint."""

import sys

from models import storage
from models.user import User

def main():
    """Main entry point for script."""
        
    if storage.all('User'):
            print ('A user already exists! Create another? (y/n): '),
            create = input()
            if create == 'n':
                return
    print ('Enter your first name: '),
    first_name = input()
    print ('Enter your last name: '),
    last_name = input()
    print ('Enter your email address: '),
    email = input()
    print ('Enter your password: '),
    password = input()

    user = User(first_name=first_name, last_name=last_name,
            email=email, password=password, is_admin=True)
    user.save()
    print ('User added.')

if __name__ == '__main__':
    sys.exit(main())