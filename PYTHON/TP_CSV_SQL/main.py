#!/usr/bin/env python3
# coding: utf-8

import argparse
import csv
import unicodedata

import database
import login
import password
import sendmail


def import_csv(bdd):
    """
    In : database (OrmManager object)
    Add new users in database, generate login/password and then them by email
    """
    # Generate logins from surname/name
    logins = login.get_logins(args.import_csv[0])

    csv_file = open(args.import_csv[0], 'r')
    reader = csv.reader(csv_file)

    i = 0  # Indice of logins list
    for cs in reader:
        if i == 0:
            pass  # Pass first line of file
        else:
            # Check if username already exists
            if not db.login_already_exists(logins[i]):
                passwd = password.Password(10)  # Create password for this user

                try:
                    # Create user
                    db.create_user(logins[i],
                                   passwd.hash,
                                   cs[0], cs[2],
                                   cs[3], cs[4],
                                   cs[5], cs[6],
                                   cs[1], cs[8],
                                   cs[7])
                    # Send email, take some time (~2sec)
                    sendmail.sendmail(cs[6], logins[i], passwd.passwd)
                except IndexError:
                    print("Empty line")
                    pass  # For empty lines in csv file
            else:
                print("User " + logins[i] + " already exists !")
        i += 1


def delete_users(db, logins):
    """
    In : database (OrmManager object), logins of users (list)
    Suppress all users from their logins
    """
    for lo in logins:
        db.delete_user(lo)


def change_group(db, login, new_group):
    """
    Change department of an user from login
    In : database (OrmManagerobject), login(str), new_group(str)
    """
    db.change_group(login, new_group)


def change_surname(db, login, new_name):
    """
    Change surname of an user from login
    In : database (OrmManager object), login(str), new_name(str)
    """
    db.change_surname(login, new_name)

if __name__ == '__main__':
    """
    Main program.
    Execute function from command line with plugin argparser
    """

    db = database.OrmManager()  # Creating databaseORM object

    # Execute from command line
    parser = argparse.ArgumentParser(description='A remplir', prog='Office')
    parser.add_argument('-i',
                        '--import_csv',
                        metavar='fichiercsv', nargs='+',
                        help='Import csv file in database.')

    parser.add_argument('-d',
                        '--delete', nargs='+',
                        help='Delete user from login.')

    parser.add_argument('-cg',
                        '--chgroup', nargs=2,
                        help='Change group of user from login.')

    parser.add_argument('-cn',
                        '--chname', nargs=2,
                        help='Change surname of user from login.')

    args = parser.parse_args()

    # Choose the good function
    if args.import_csv:
        import_csv(db)
    elif args.delete:
        delete_users(db, args.delete)
    elif args.chgroup:
        change_group(db, args.chgroup[0], args.chgroup[1])
    elif args.chname:
        change_surname(db, args.chname[0], args.chname[1])
