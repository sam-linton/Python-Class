#
# Rock
#
from Actor import Actor

class Rock(Actor):
    """
    Implement Rock class that does nothing
    
    """
    
    def __init__(self, image_filename='rock.png'):
        """
        Initialize
        
        """
        super().__init__(image_filename = image_filename)
    
    
    def act(self)-> None:
        """
        Act for a single timestep.
        
        """
        pass