from bug import Bug
from actor import Actor, NORTH

class SquareBug(Bug):
    '''
    SquareBug class
    
    '''
    
    def __init__(self, length, image_filename='images/bug1.png', direction = NORTH) -> None:
        '''
        Initialize
        Note that length is the number of steps, not
        the number of cells
        
        '''
        super().__init__(image_filename, direction)
        self.count = 0
        self.length = length
    
    def act(self) -> None:
        '''
        Act method, called every timestep
        
        '''
        if self.count >= self.length:
            self.turn_left()
            self.count = 0
        else:
            super().act()
            self.count += 1

        
        

