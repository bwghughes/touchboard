#!/usr/bin/python

# <card.py>
# Created: January 10, 2011
# Version: 0.0.1
# By: Ben Hughes (bwghughes@gmail.com)
from logbook import Logger
log = Logger('app')
######################################################
#
# Card 
#
######################################################

from models.card import Card, CardEvent

"""
    The job of this class is to cerate a crd event based on
    some simple rules. These are:
    1. If a tag has no story_id associated to it, it should be registered.
    2. TODO: If a card has no story points it should not be allowed to register - On Hold
    3. If a card is done it can be unregistered.
    4. The status should be updated if the card is registered and has points.
"""
class CardEventDispatcher(object):
    def __init__(self, card):
        self.card = card
        
    def dispatch(self):
        if not self.card.story_id:
            log.info('No story_id - registering...')
            action = 'register'
        elif:
            
        ce = CardEvent(self.card, action)

def main():
    """docstring for main"""
    log.info('Starting touchboard job processor...')
    # Connect to HotQueue
    # Process Jobs.


if __name__ == '__main__':
    
    main()