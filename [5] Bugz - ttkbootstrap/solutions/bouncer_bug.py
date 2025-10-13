from bug import Bug
from actor import Actor, NORTH

class BouncerBug(Bug):
    '''
    BouncerBug class
    
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
        if self.can_move():
            self.move()
        else:
            self.turn_around()
