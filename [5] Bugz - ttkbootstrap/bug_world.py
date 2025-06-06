#
# BugWorld
#
from world import World
from app_state import AppState
from actor import NORTH, EAST, SOUTH, WEST
from bug import Bug
from flower import Flower
from rock import Rock
from spinner_bug import SpinnerBug
from bouncer_bug import BouncerBug
from tired_bug import TiredBug
from dying_bug import DyingBug



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
        # Use the command below to add actors 1 at at time
        self.add(DyingBug(max_steps=5), 5, 5, NORTH)
        self.add(Bug(),8, 8, SOUTH)
        
        # Add multiple actors
#         self.add_multiple_actors([
#             (Bug(), 0, 0, SOUTH),
#             (Bug(), 5, 5, NORTH)
#             ])

        
        # Add actors randomly
        self.add_random_actors(num_rocks = 10,
                               num_flowers = 20,
                               num_bugs = 0)
        

