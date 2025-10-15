#
# BugWorld
#
from world import World
from app_state import AppState
from actor import NORTH, EAST, SOUTH, WEST
from bug import Bug
from flower import Flower
from rock import Rock


class BugWorld(World):
    '''
    World - holds all active actors
    
    '''
    
    def __init__(self, parent, app_state: AppState) -> None:
        '''
        Initialize
        
        '''
        super().__init__(parent, app_state)
        
        
    def add_actors(self) -> None:
        '''
        Add actors to this world. Change this to add desired actors.
        
        '''
        
        # Add actors randomly
        self.add_random_actors(num_rocks = 10,
                               num_flowers = 20,
                               num_bugs = 0)
        
        
        self.replace_ok = True

        # Add your own bug(s) by replacing this command
        # Make sure to add any needed import commands at the top of this file
        self.add(Bug(),8, 8, SOUTH)


        self.replace_ok = False
        
