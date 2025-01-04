#
# Bug
#
from actor import Actor, NORTH


class Bug(Actor):
    '''
    Bug class
    
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
        if self.can_move():
            self.move()
        else:
            self.turn_left()