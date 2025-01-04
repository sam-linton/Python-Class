#
# Flower
#
from Actor import Actor

class Flower(Actor):
    """
    Implement Flower class that does nothing
    
    """
    
    def __init__(self, image_filename='flower1.png'):
        """
        Initialize
        
        """
        super().__init__(image_filename = image_filename)
    
    
    def act(self)-> None:
        """
        Act for a single timestep.
        
        """
        pass