#!/usr/bin/env python3
# coding: utf-8

import os
import sys

import sqlalchemy

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class OrmManager():
    """
    ORM
    Links with sqlite database, use sqlalchemy
    """
    def __init__(self):
        # Create db and tables
        self.engine = create_engine('sqlite:///office.db')
        Base.metadata.create_all(self.engine)

        # Use engine
        Base.metadata.bind = self.engine

        # Create session
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

        # functions / Departments
        departments = ['Info', 'Direction', 'DSI', 'Comptabilité', 'Helpdesk']
        functions = ['ITWO', 'RH', 'Directeur', 'Assistant', 'Assistante',
                     'Responsable', 'Comptable', 'Informatique', 'stagiaire']

        # Create functions and departments
        try:
            self.create_departments(departments)
            self.create_functions(functions)
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()
        except sqlalchemy.exc.InvalidRequestError:
            self.session.rollback()

    def login_already_exists(self, login):
        """
        Check if login is already present in database
        In : login (str)
        """
        try:
            login = self.session.query(self._User)\
                .filter(self._User.login == login).one()
        except sqlalchemy.orm.exc.NoResultFound:
            return False
        return True

    def get_department_from_name(self, name):
        """
        Return department object from name
        In : name of department(string)
        """
        try:
            dep = self.session.query(self._Department)\
                .filter(self._Department.name == name).one()
            return dep
        except sqlalchemy.orm.exc.NoResultFound:
            print("Department " + name + " was not found in base ! \
                Please add it using command office add department " + name)
            self.session.rollback()
            return None

    def get_function_from_name(self, name):
        """
        Return function object from name
        In : name of function (string)
        """
        try:
            func = self.session.query(self._Function)\
                .filter(self._Function.name == name).one()
            return func
        except sqlalchemy.orm.exc.NoResultFound:
            self.session.rollback()
            print("Function " + name + " was not found in base ! \
                Please add it using command office add function "+name)
            return None

    def create_departments(self, departments):
        """
        Create departments
        In : list of departments
        """
        try:
            for dep in departments:
                tmp = self._Department(name=dep)
                self.session.add(tmp)
            self.session.commit()
        except:
            self.session.rollback()

    def create_functions(self, functions):
        """
        Create functions
        In : list of functions
        """
        try:
            for func in functions:
                tmp = self._Function(name=func)
                self.session.add(tmp)
            self.session.commit()
        except:
            self.session.rollback()

    def create_user(self, login, passwd, surname,
                    name, birthdate, function,
                    department, email, oldname=None,
                    mobile=None, phone=None):
        """
        Create users
        In : all user infos (string)
        """

        # Check if department and function exists
        dep = self.get_department_from_name(department)
        func = self.get_function_from_name(function)

        if dep is not None and func is not None:
            try:
                user = self._User(login=login, passwd=passwd,
                                  surname=surname, name=name,
                                  birthdate=birthdate, email=email,
                                  function=func.name, department=dep.name,
                                  mobile=mobile, phone=phone, oldname=oldname)
                self.session.add(user)
                self.session.commit()
                print("User " + login + " successfully added !")
            except sqlalchemy.exc.IntegrityError as e:
                print("Something went wrong when adding this user.")
                print(str(e))
                self.session.rollback()
        else:
            print("User "+login+" wasn't created")
            self.session.rollback()

    def delete_user(self, login):
        """
        Delete an user from login
        In : login (string)
        """

        try:
            user = self.session.query(self._User)\
                .filter(self._User.login == login).one()
            self.session.delete(user)
            self.session.commit()
            print("User "+login+" was deleted.")
        except sqlalchemy.orm.exc.NoResultFound:
            self.session.rollback()
            print("Username " + login + " was not found in base !")

    def change_group(self, login, group):
        """
        Modify group of an user
        In : login (string)
        """
        try:
            user = self.session.query(self._User)\
                .filter(self._User.login == login).one()
            user.department = group
            self.session.commit()
            print("Group of user "+login+" was updated.")
        except sqlalchemy.orm.exc.NoResultFound:
            self.session.rollback()
            print("Username " + login + " was not found in base !")

    def change_surname(self, login, surname):
        """
        Change surname of an user
        In : surname (string)
        """
        try:
            user = self.session.query(self._User)\
                .filter(self._User.login == login).one()
            user.surname = surname
            self.session.commit()
            print("Surname of user "+login+" was updated.")
        except sqlalchemy.orm.exc.NoResultFound:
            self.session.rollback()
            print("Username " + login + " was not found in base !")

    class _Function(Base):
        """
        Used in order to create table functions
        """
        __tablename__ = 'functions'
        name = Column(String(64), nullable=False, primary_key=True)

    class _Department(Base):
        """
        Used in order to create table departments
        """
        __tablename__ = 'department'
        name = Column(String(64), nullable=False, primary_key=True)

    class _User(Base):
        """
        Used in order to create table users
        """
        __tablename__ = 'users'
        login = Column(String(64), nullable=False, primary_key=True)
        passwd = Column(String(64), nullable=False)
        surname = Column(String(64), nullable=False)
        oldname = Column(String(64), nullable=True)
        name = Column(String(64), nullable=False)
        birthdate = Column(String(64), nullable=False)
        email = Column(String(64), nullable=False)
        phone = Column(String(10), nullable=True)
        mobile = Column(String(10), nullable=True)
        function = Column(String(64), ForeignKey('functions.name'))
        department = Column(String(64), ForeignKey('department.name'))
