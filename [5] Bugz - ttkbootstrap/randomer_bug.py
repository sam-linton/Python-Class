from bug import Bug
from actor import Actor, NORTH
from random import randint

class RandomerBug(Bug):
    '''
    RandomerBug class
    
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
            test = randint(1, 100)
            if test <= 80:
                self.move()
            elif test <= 90:
                self.turn_left()
            else:
                self.turn_right()
        else:
            test = randint(0, 1)
            if test == 0:
                self.turn_left()
            else:
                self.turn_right()
