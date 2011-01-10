#!/usr/bin/python

# <test_filename.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)

import os
import sys
from nose.tools import *
from mock import Mock, patch, MagicMock

class TestCardEventDispatcher(object):
    """docstring for TestApp"""
    def __init__(self, arg):
        pass
        
    def setup(self):
        pass

    def teardown(self):
        pass    
        
    @patch('models.card.Card')
    def test_