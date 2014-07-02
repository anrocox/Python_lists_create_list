#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

How do you define a list in python?

¿Como se puede crear una lista en python?
'''

#create an empty list
lista = []
print (lista)

#create a list with numbers
lista = [1, 2, 3, 4, 5]
print (lista)

#create a list with string data
lista = ['a', 'b', 'c', 'd', 'e']
print (lista)

#create a list with different data types
lista = [1, 'hello', True, 'a', 2.0]
print (lista)

#create an empty list with list() function of built-in python
lista = list()
print (lista)

#create a list from a tuple
lista = list((1, 2, 3))
print (lista)

#create a list from a str
lista = list('hello')
print (lista)
