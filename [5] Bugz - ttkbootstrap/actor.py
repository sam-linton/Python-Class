#
# Actor
#
from __future__ import annotations
import ttkbootstrap as ttk
from PIL import Image, ImageTk

NORTH: int = 0
EAST: int = 90
SOUTH: int = 180
WEST:int = 270


class Actor:
    '''
    Base class for everything that exists in the world.
    
    '''
    
    def __init__(self, image_filename='images/bug1.png', direction = NORTH) -> None:
        '''
        Initialize
        
        '''
        self.i: int = 0
        self.j: int = 0
        self.world = None
        self.direction = direction
        self.size = 1
        self.image_original: Image = Image.open(image_filename)
        self.update_image()
        
    def update_image(self) -> None:
        '''
        Retrieve and scale image
        
        '''
        self.image_resized: Image = self.image_original.resize((self.size, self.size)).rotate(360-self.direction)
        self.image: ImageTk = ImageTk.PhotoImage(self.image_resized)
        
    def resize(self, size) -> None:
        '''
        Resize to given size
        
        '''
        if size <= 0: return
        self.size = size
        self.update_image()
    
    def draw(self, canvas: ttk.Canvas) -> None:
        '''
        Draw self on canvas
        
        '''
        if not self.world is None:
            x = self.world.get_x(self.i)
            y = self.world.get_y(self.j)
            canvas.create_image(x, y, anchor = 'nw', image = self.image)
            
    def set_direction(self, direction: int) -> None:
        '''
        Set direction the actor is facing.
        
        '''
        self.__turn_by(direction - self.direction)

    def act(self) -> None:
        '''
        Override this in base classes. It is called every timestep
        
        '''
        pass
    
    def get_i(self) -> int:
        '''
        Return i coordinate
        
        '''
        return self.i
    
    def get_j(self) -> int:
        '''
        Return j
        '''
        return self.j
    
    def get_direction(self) -> int:
        '''
        Return direction
        '''
        return self.direction
            
    def get_next_i(self) -> int:
        '''
        Get i-index in the direction the actor is facing
        
        '''
        if self.direction == EAST: return self.i+1
        elif self.direction == WEST: return self.i-1
        else: return self.i
    
    def get_next_j(self) -> int:
        '''
        Get j-index in the direction the actor is facing
        
        '''
        if self.direction == NORTH: return self.j-1
        elif self.direction == SOUTH: return self.j+1
        else: return self.j
    
    def __turn_by(self, degrees: int) -> None:
        '''
        Turn by the given number of degrees clockwise
        
        '''
        self.direction = (self.direction + degrees) % 360
        self.update_image()
    
    def turn_left(self) -> None:
        '''
        Turn left relative to current direction
        
        '''
        self.__turn_by(270)
        
    def turn_right(self) -> None:
        '''
        Turn right relative to current location
        '''
        self.__turn_by(90)
        
    def turn_around(self) -> None:
        '''
        Turn to face the opposite direction
        
        '''
        self.__turn_by(180)
    
    def can_move(self) -> bool:
        '''
        True if the actor is in the world, and the space in front is clear.
        
        '''
        if self.world is None:
            return False
        return self.world.is_available(self.get_next_i(), self.get_next_j())
    
    def move(self) -> bool:
        '''
        Move to the space that the actor is facing. Returns True if successful
        
        '''
        if self.world is None:
            print('Error: Attempt to move actor not in the world.')
            return False
        return self.world.move_actor_to(self, self.get_next_i(), self.get_next_j())
    
    def set_world(self, world) -> None:
        '''
        Save a reference to the world.
        
        '''
        self.world = world
        
    def get_world(self) -> World | None:
        '''
        Return the world (or None)
        
        '''
        return self.world
        
    def is_in_world(self) -> bool:
        '''
        Return true if the actor is in the world.
        
        '''
        return not self.world is None

    def get_neighbor(self) -> Actor | None:
        '''
        Get neighbor in the space that the actor is facing. May be None
        
        '''
        if self.world is None:
            return None
        return self.world.get_actor(self.get_next_i(), self.get_next_j())
    
    def remove_self_from_world(self) -> None:
        '''
        Remove self from the world
        
        '''
        if self.world == None:
            return
#         self.world = None
        self.world.remove(self)
