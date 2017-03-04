#!/usr/bin/env python3
# coding: utf-8

import os
import sys

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Fonction(Base):
    __tablename__ = 'fonctions'
    name = Column(String(64), nullable=False, primary_key=True)

class Department(Base):
    __tablename__ = 'department'
    name = Column(String(64), nullable=False, primary_key=True)

class User(Base):
    __tablename__ = 'users'
    login = Column(String(64), nullable=False, primary_key=True)
    surname = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    oldname = Column(String(64), nullable=True)
    birthdate = Column(String(64), nullable=False)
    passwd = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    phone = Column(String(10), nullable=True)
    mobile = Column(String(10), nullable=True)
    fonction = Column(String(64), ForeignKey('fonctions.name'))
    department = Column(String(64), ForeignKey('department.name'))

def get_user(login):
    user = session.query(User).filter(User.login == login).one()
    #return user.surname, user.name, user.email, 

if __name__ == '__main__':

    ## Create db and tables
    engine = create_engine('sqlite:///sqlalchemy_example.db')
    Base.metadata.create_all(engine)
        ## Use engine
    Base.metadata.bind = engine

    ## Create session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    ## Create departments 
    departments = ['direction', 'RH', 'DSI']
    for dep in departments:
        tmp = Department(name = dep)
        session.add(tmp)
    fonctions = ['RH', 'ITWO']
    for fo in fonctions:
        tmp = Fonction(name = fo)
        session.add(tmp)
    session.commit()
    

    direction = session.query(Department).filter(Department.name == 'direction').one()

    ## Create fonctions
    rh = session.query(Fonction).filter(Fonction.name == 'RH').one()
    
    print(direction.name)
    #p1 = User(login='arfag', surname='Rfag', name = 'Adèle', passwd='1111111111111111111111111111111111111111', email='adele.arfag@mail.com', fonction=rh.name, department=direction.name)
    #session.add(p1)
    
    session.commit()
