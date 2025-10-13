from bug import Bug
from actor import Actor, NORTH

class TiredBug(Bug):
    '''
    TiredBug class
    
    '''
    
    def __init__(self, max_steps, image_filename='images/bug1.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)
        self.count = 0
        self.max_steps = max_steps
    
    def act(self) -> None:
        '''
        Act method, called every timestep
        
        '''
        
        if self.count >= self.max_steps:
            return
        
        super().act()
#         if self.can_move():
#             self.move()
#         else:
#             self.turn_left()
            
        self.count += 1
        
        
