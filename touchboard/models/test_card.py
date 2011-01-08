#!/usr/bin/python

# <test_filename.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)

import os
import sys
from nose.tools import *
from mock import Mock, patch, MagicMock

from card import Card


class TestCard(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def setup(self):
        self.card = Card(tag=Mock(), story_id=Mock(), points=Mock(), status='Planned')

    def teardown(self):
        pass
    
    @patch('card.statuses', spec=MagicMock)
    def test_card_has_all_the_necessaries(self, mock_statuses):    
        assert self.card.tag
        assert self.card.story_id
        assert self.card.points
        assert self.card.status
        
    @raises(ValueError) 
    def test_raises_error_if_tag_is_none(self):
        card = Card(tag=None, story_id=Mock(), points=Mock(), status='Planned')

    @raises(ValueError) 
    def test_raises_error_if_story_id_is_none(self):
        card = Card(tag=Mock(), story_id=None, points=Mock(), status='Planned')

    @raises(ValueError) 
    def test_raises_error_if_points_is_none(self):
        card = Card(tag=Mock(), story_id=Mock(), points=None, status='Planned')

    @raises(ValueError) 
    def test_raises_error_if_status_is_none(self):
        card = Card(tag=Mock(), story_id=Mock(), points=Mock(), status=None)
        
    def test_card_id_is_valid(self):
        assert isinstance(self.card.card_id, str)
        assert len(self.card.card_id.split(':')) > 0
        
    @raises(ValueError) 
    def test_card_is_invalid_with_invalid_status(self):
        card = Card(tag=Mock(), story_id=Mock(), points=Mock(), status='Thingummy')