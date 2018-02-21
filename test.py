from math import *
import eventlet
import mock
import flake8
import sphinx

def my_func():
    print sqrt(4)
    print 'called'


alias = my_func
my_list = [1, None, alias]
inception = my_list[2]

inception()
