#
# Rock
#
from actor import Actor, NORTH


class Rock(Actor):
    '''
    Rock - does nothing
    
    '''
    def __init__(self, image_filename='images/rock.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)