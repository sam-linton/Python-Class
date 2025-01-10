from bug import Bug
from actor import Actor, NORTH
from random import randint

class RandomBug(Bug):
    '''
    RandomBug class
    
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
            test = randint(0, 2)
            if test == 0:
                self.turn_left()
            elif test == 1:
                self.turn_right()
            else:
                self.turn_around()
