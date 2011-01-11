#!/usr/bin/python

# <card.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)
from logbook import Logger
log = Logger('reader')
######################################################
#
# Card 
#
######################################################
"""
    The job of this class is to act as a Card.
"""
class Reader(object):
    """docstring for Reader"""
    def __init__(self, reader_id):
        #TODO Load from Config
        self.reader_id = reader_id
        

class RegisterReader(Reader):
    """docstring for RegisterableReader"""
    def __init__(self, arg):
        super(Reader, self).__init__()
        self.arg = arg
        

class StatusReader(Reader):
    """docstring for RegisterableReader"""
    def __init__(self, arg):
        super(Reader, self).__init__()
        self.arg = arg
        