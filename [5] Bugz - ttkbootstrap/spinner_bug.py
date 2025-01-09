from bug import Bug
from actor import Actor, NORTH

class SpinnerBug(Bug):
    '''
    SpinnerBug class
    
    '''
    
    def __init__(self, image_filename='images/bug2.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)
    
    def act(self) -> None:
        '''
        Act method, called every timestep
        
        '''
        self.turn_left()