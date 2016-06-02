#!/usr/bin/env python

from random import choice

class GeneratePassword(object):

    _characters = [
        'abcdefghijklmnopqrstuvwxyz',
        '0123456789',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '!@#$%^&*()_+-=[]{}|'
        ]

    @staticmethod
    def getpassword(length=25):
        password = []
        charset = choice(GeneratePassword._characters)
        while len(password) < length:
            password.append(choice(charset))
            charset = choice(list(set(GeneratePassword._characters) - set([charset])))
        return "".join(password)
