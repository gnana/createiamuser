#!/usr/bin/env python

import argparse
from iamuser import IAMUser
from password import GeneratePassword

def main():

    parser = argparse.ArgumentParser(description='Tool to create AWS IAM Users')
    parser.add_argument('--username', required=True, help='IAM usernames to create')
    parser.add_argument('--role', help='Role to be assigned to the user')
    parser.add_argument('--password-only', action='store_true', help='Creates only Password')
    parser.add_argument('--accesskey-only', action='store_true', help='Creates only Access/Secret keys')
    args = parser.parse_args()

    users = args.username.split(",")
    for user in users:
        newuser = IAMUser(user, args.role, args.password_only, args.accesskey_only)
        if newuser.createuser():
            print ("Username: %s" % newuser.username)
            if newuser.password is not None:
                print ("Password: %s" % newuser.password)
            if newuser.accesskey is not None:
                print ("AccessKey: %s" % newuser.accesskey)
            if newuser.secretkey is not None:
                print ("SecretKey: %s" % newuser.secretkey)
            if newuser.groups:
                print ("Groups: %s" % newuser.groups)
            print("")

if __name__ == "__main__":
    main()
