from bug import Bug
from actor import Actor, NORTH

class DyingBug(Bug):
    '''
    Dying class
    
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
        if not self.world == None:
            i, j = self.world.get_next_coords((self.get_i(), self.get_j()), self.get_direction())
            print(f'{i}, {j}')
            
        if not self.is_in_world():
            return
        
        if self.count >= self.max_steps:
            self.remove_self_from_world()
            return
            
        super().act()
            
        self.count += 1
        
        

