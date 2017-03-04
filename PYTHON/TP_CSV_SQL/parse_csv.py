#!/usr/bin/env python3
# coding: utf-8

import unicodedata
import csv

import consult-db

def normalize(name):
    name = name.lower()
    #ascii_byte = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore' )
    #uni = ascii_byte.decode("utf-8")
    name = name.replace('-', '')
    name = name.replace(' ', '')
    return name

def generate_login(n1, p, n2=None):
    n1 = normalize(n1)
    p = normalize(p)
    if n2 is not None:
        n2 = normalize(n2)
        return p[0] + n1[0:6] + n2[0]
    return p[0] + n1[0:6]

def generate_user_from_csv():
    csv_file = open('test.csv', 'r')
    reader = csv.reader(csv_file)
    logins = list()
    for raw in reader:
        login = generate_login(raw[0], raw[2])
        logins.append(login)
        #print(login)

    return logins
