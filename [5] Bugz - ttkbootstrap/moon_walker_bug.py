from bug import Bug
from actor import Actor, NORTH

class MoonWalkerBug(Bug):
    '''
    MoonWalkerBug class
    
    '''
    
    def __init__(self, image_filename='images/bug1.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)
    
    def act(self) -> None:
        '''
        Act method, called every timestep
        
        '''
        self.turn_around()
        if self.can_move():
            self.move()
            self.turn_around()
        else:
            # Or turn_left
            self.turn_around()
            self.turn_right()

