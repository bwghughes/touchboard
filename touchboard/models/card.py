#!/usr/bin/python

# <card.py>
# Created: January 7, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)




######################################################
#
# Card 
#
######################################################
"""
    The job of this class is to process Card stuff
"""
class Card(object):
    """Represents a card object"""
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            if v is None:
                raise ValueError('%s cannot have a value of None.' % str(k))

            if str(k) is 'status':
                if v not in statuses:
                    raise ValueError('%s is not a valid status' % str(v))
            
            setattr(self, k, v)

    @property
    def card_id(self):
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
    event_types = sorted({1:'register', 1:'unregister', 2:'state_change'})
    
    def __init__(self, card, event_type):        
        self.event_type = event_type
        self.card = card
        
    def process(self):
        self.__call__('_%s' % self.event_type) 
        
    def _register(self):
        pass
        
    def _unregister(self):
        pass
        
    def _state_change(self):
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
        