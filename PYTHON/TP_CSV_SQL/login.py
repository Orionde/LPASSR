#!/usr/bin/env python3
# coding: utf-8

import unicodedata
import csv

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

def get_logins(filename):
    csv_file = open(filename, 'r')
    reader = csv.reader(csv_file)
    logins = list()
    try:
        for raw in reader:
            login = generate_login(raw[0], raw[2])
            logins.append(login)

    except IndexError:
        pass # For empty lines

    return logins

