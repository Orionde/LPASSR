#!/usr/bin/env python3
# coding: utf-8

import argparse
import csv
import unicodedata

import database
import login
import password
import sendmail

"""NOM,NOM de jeune fille,Prénom,Date de naissance,Fonction,Département,Courriel,Téléphone,Mobile"""
"""
0 : Nom
1 : Nom jeune fille
2 : prenom
3 : naissance
4 : fonction
5 : department
6 : email
7 : tel
8 : mobile

"""
def import_csv(bdd):
    logins = login.get_logins(args.import_csv[0])
    csv_file = open(args.import_csv[0], 'r')
    reader = csv.reader(csv_file)
    i = 0
    for cs in reader:
        if i == 0:
            pass # Pass first line of file
        else:
            if not db.login_already_exists(logins[i]):
                passwd = password.Password(10) # Create password for this user
                sendmail.sendmail(cs[6], logins[i], passwd.passwd)

                try:
                    db.create_user(logins[i], passwd.hash, cs[0], cs[2], cs[3], cs[4], cs[5], cs[6], cs[1], cs[8], cs[7])
                except IndexError:
                    print("Empty line")
                    pass # For empty lines
            else:
                print("User " + logins[i] + " already exists")
        i += 1

def delete_users(db, logins):
    for lo in logins:
        db.delete_user(lo)

def change_group(db, login, new_group):
    db.change_group(login, new_group)

def change_surname(db, login, new_name):
    db.change_surname(login, new_name)

## Main program
if __name__ == '__main__':
    db = database.OrmManager()
    parser = argparse.ArgumentParser(description='A remplir', prog='Office')
    parser.add_argument('-i','--import_csv', metavar='fichiercsv', nargs='+',
                    help='Import csv file in database. Usage: office -i file.csv')

    parser.add_argument('-d', '--delete', nargs='+',
                    help='Delete user from login. Usage: office -i login1 login2')

    parser.add_argument('-cg', '--chgroup', nargs=2,
                    help='Change group of user from login. Usage: office -cg login newgroup')

    parser.add_argument('-cn', '--chname', nargs=2,
                    help='Change surname of user from login. Usage: office -cn login newgroup')

    args = parser.parse_args()

    if args.import_csv:
        import_csv(db)
    elif args.delete:
        delete_users(db, args.delete)
    elif args.chgroup:
        change_group(db, args.chgroup[0], args.chgroup[1])
    elif args.chname:
        change_surname(db, args.chname[0], args.chname[1])
