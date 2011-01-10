#!/usr/bin/python

# <test_filename.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)

import os
import sys
from nose.tools import *
from mock import Mock, patch, MagicMock

from models.card import Card, CardEvent

class TestCard(object):

    def test_card_has_all_the_necessaries(self):    
        card = Card(tag=Mock(), story_id=Mock(), points=Mock(), status='Planned')
        assert card.story_id
        assert card.points
        assert card.status
        assert card.card_id

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
        card = Card(tag=Mock(), story_id=Mock(), points=Mock(), status='Planned')
        assert isinstance(card.card_id, str)
        assert len(card.card_id.split(':')) > 0


class TestCardEvent(object):
    """docstring for TestCardEvent"""
    def setup(self):
        pass
                
    def teardown(self):
        pass
    
    @patch('models.card.Card')
    @patch('models.card.log')
    @patch.object(CardEvent, '_register')
    def test_register_is_processed_when_reg_called(self, mock_card, mock_log, mock_register):
        ce = CardEvent(mock_card, 'register')
        ce.process()
        assert ce._register.called
        assert mock_card.called
        assert mock_log.info.called
        
    @patch('models.card.Card')
    @patch('models.card.log')
    @patch.object(CardEvent, '_unregister')
    def test_unregister_is_processed_when_unreg_called(self, mock_card, mock_log, mock_unregister):
        ce = CardEvent(mock_card, 'unregister')
        ce.process()
        assert ce._unregister.called
        assert mock_card.called
        assert mock_log.info.called

    @patch('models.card.Card')
    @patch('models.card.log')
    @patch.object(CardEvent, '_state_change')
    def test_state_change_is_processed_when_state_change_called(self, mock_card, mock_log, mock_unregister):
        ce = CardEvent(mock_card, 'state_change')
        ce.process()
        assert ce._state_change.called
        assert mock_card.called
        assert mock_log.info.called

    @raises(AttributeError)
    @patch('models.card.log')
    @patch('models.card.Card')
    def test_process_fails_when_non_existent_event(self, mock_card, mock_log):
        ce = CardEvent(mock_card, 'non_existent_event_type')
        ce.process()
        assert mock_log.error.called
        