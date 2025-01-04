#
# Bug
#
from Actor import Actor

class Bug(Actor):
    """
    Superclass for all bugs
    
    """
    
    def __init__(self, image_filename='bug1.png'):
        """
        Initialize
        
        """
        super().__init__()
        
    def act(self)-> None:
        """
        Action for a single step
        
        """
        if self.can_move():
            self.move()
        else:
            self.turn_left()
        #print(f'({self.i},{self.j},{self.direction})')