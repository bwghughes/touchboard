#!/usr/bin/python

# <card.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)
from logbook import Logger
log = Logger('card')
######################################################
#
# Card 
#
######################################################
"""
    The job of this class is to act as a Card.
"""
class Card(object):
    """Represents a card object"""
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            if v is None:
                raise ValueError('%s cannot have a value of None.' % str(k))
            setattr(self, k, v)

    @property
    def card_id(self):
        if self.tag and self.story_id:
            return '%s:%s' % (str(self.tag), str(self.story_id))

######################################################
#
# Card Event
#
######################################################
"""
    The job of this class is to process Card Events
"""
class CardEvent(object):
    """docstring for CardEvent"""
    
    card_states = sorted({0:'Unregistered', 1:'Planned', 2:'In Progress', 3:'In QA', 4:'Done'})
    
    def __init__(self, card, event_type):        
        self.event_type = event_type
        self.card = card
        
    def process(self):
        log.info('Processing card event for %s' % self.card)
        try:
            event = '_%s' % self.event_type
            getattr(self, event)()
        except AttributeError:
            log.error('Cannot find card event method %s' % event)
            raise
        
    def _register(self, tag, story_id):
        log.info('Registering card %s' % self.card)
        pass
            
    def _unregister(self):
        log.info('Unegistering card %s' % self.card)
        pass
        
    def _state_change(self):
        log.info('Changing state for card %s' % self.card)
        pass

######################################################
#
# Card History
#
######################################################
"""
    The job of this class is to keep card history
"""
class CardHistory(object):
    """ The job of this object is to record a Card's history """
    def __init__(self, **kwargs):
        self.card_id = card_id
        self.status = status
        self.last_updated = last_updated
        