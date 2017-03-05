#!/usr/bin/env python3
# coding: utf-8

import unicodedata
import csv


def normalize(name):
    """
    Set name in lovercase, remove '-' and ' '
    In : name (string)
    """
    name = name.lower()
    name = name.replace('-', '')
    name = name.replace(' ', '')
    return name


def generate_login(n1, p, n2=None):
    """
    Generate login : keep 1 letter name,
        6 first letters surname and 1 letter oldname
    In : surname, name and oldname (string)
    """
    n1 = normalize(n1)
    p = normalize(p)
    if n2 is not None:
        n2 = normalize(n2)
        return p[0] + n1[0:6] + n2[0]
    return p[0] + n1[0:6]


def get_logins(filename):
    """
    Read csv file and create logins
    In : filename (string)
    """
    csv_file = open(filename, 'r')
    reader = csv.reader(csv_file)
    logins = list()
    try:
        for raw in reader:
            login = generate_login(raw[0], raw[2])
            logins.append(login)

    except IndexError:
        pass  # For empty lines

    return logins
