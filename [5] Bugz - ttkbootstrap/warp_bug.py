from bug import Bug
from actor import Actor, NORTH
from random import randint, choice

class WarpBug(Bug):
    '''
    WarpBug class
    
    '''
    
    def __init__(self, image_filename='images/bug1.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        super().__init__(image_filename, direction)
    
    
    def act(self) -> None:
        '''
        Act method, called every timestep
        
        '''
        world = self.get_world()
        if world == None:
            return
        
        # Method 1:
        '''
        count = 0 # Avoid an infinite loop
        while count < 100:
            count += 1
            i = randint(0, world.get_imax())
            j = randint(0, world.get_jmax())
            if world.is_available(i, j):
                world.move_actor_to(self, i, j)
                return
        '''
            
        cell_indices = []
        for i in range(world.get_imax()+1):
            for j in range(world.get_jmax()+1):
                if world.is_available(i, j):
                    cell_indices.append((i, j))
                    
        if len(cell_indices) == 0:
            return
        
        i, j = choice(cell_indices)
        world.move_actor_to(self, i, j)
        