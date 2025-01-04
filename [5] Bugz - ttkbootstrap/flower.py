#
# Flower
#
from actor import Actor, NORTH


class Flower(Actor):
    '''
    Flower actor: doesn't move
    
    '''
    
    def __init__(self, image_filename='images/flower1.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)