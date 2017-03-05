import random
import hashlib
import smtplib


class Password:
    def __init__(self, size):
        self.passwd = self._generate(size)
        self.hash = self._hash(self.passwd)

    def _generate(self, size):
        element = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\
            abcdefghijklmnopqrstuvwxyz0123456789+-*/$%&.:?!"
        passwd = ""
        for i in range(size):
            passwd = passwd + element[random.randint(0, len(element)-1)]
        return passwd

    def _hash(self, passwd):
        passwd_sha1 = hashlib.sha1(passwd.encode())
        passwd_hash = passwd_sha1.hexdigest()

return passwd_hash
