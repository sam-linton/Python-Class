#
# Actor
#
from tkinter import *
from PIL import Image,ImageTk
import PySimpleGUI as sg

# Directions
NORTH: int = 0
EAST: int = 90
SOUTH: int = 180
WEST:int = 270
    

class Actor:
    """
    Superclass for all actors in the world.

    """

    def __init__(self, image_filename='bug1.png'):
        """
        Initialize
        
        """
        self.i = 0
        self.j = 0
        self.direction = NORTH
        self.world = None
        self.img = Image.open(image_filename)
        self.img = self.img.resize((20, 20))
        self.img = self.img.rotate(self.direction)

    def draw(self, canvas: sg.Canvas)-> None:
        """
        Draw the actor
        
        """
        if not self.world is None:
            x = self.world.get_x(self.i)
            y = self.world.get_y(self.j)
            self.image = ImageTk.PhotoImage(self.img)
            canvas.create_image(x,y,anchor=NW, image=self.image)
                   
    def set_direction(self, direction: int)-> None:
        """
        Set the direction of the actor
        
        """
        self.img = self.img.rotate(self.direction - direction)
        self.direction = direction
    

    def act(self)-> None:
        """
        Intended to be overriden by subclasses to act for one timestep
        
        """
        pass
            
    def get_next_i(self)-> int:
        """
        Get i value of cell this actor is facing
        
        """
        if self.direction == EAST: return self.i+1
        elif self.direction == WEST: return self.i-1
        else: return self.i
    
    
    def get_next_j(self)-> int:
        """
        Get j value of cell this actor is facing
        
        """
        if self.direction == NORTH: return self.j-1
        elif self.direction == SOUTH: return self.j+1
        else: return self.j
    
    
    def turn_by(self, degrees: int)-> None:
        """
        Turn this actor by the provided number of degrees. Note:
        this is an internal function. Resulting angles should be
        multiples of 90 degrees.
        
        """
        self.direction = (self.direction + degrees) % 360
        self.img = self.img.rotate(-degrees)
    
    
    def turn_left(self)-> None:
        """
        Turn this actor left (by 90 degrees)
        
        """
        self.turn_by(270)
        
        
    def turn_right(self)-> None:
        """
        Turn this actor right (by 90 degrees)
        
        """
        self.turn_by(90)
        
        
    def turn_around(self)-> None:
        """
        Turn this actor around (180 degrees)
        
        """
        self.turn_by(180)
    
    
    def can_move(self)-> bool:
        """
        Return true if this actor can move: the actor is in the world and the cell ahead is available.
        
        """
        if self.world is None:
            return False
        return self.world.is_available(self.get_next_i(), self.get_next_j())

    
    def move(self)-> bool:
        """
        Move to the cell directly in front
        
        """
        if self.world is None:
            print('Error: Attempt to move actor not in the world.')
            return False
        return self.world.move_actor_to(self, self.get_next_i(), self.get_next_j())
 
        
    def set_world(self, world)-> None:
        """
        Add the actor to the provided world
        
        """
        self.world = world
        
        
    def is_in_world(self)-> bool:
        """
        Return true if the actor is in a world.
        
        """
        return not self.world is None
    

    def get_neighbor(self):
        """
        Get the neighbor in the cell ahead (or None if it doesn't exist)
        
        """
        if self.world is None:
            return None
        return self.world.get_actor(self.get_next_i(), self.get_next_j())
        
    
    def remove_self_from_world(self)-> None:
        """
        Remove self from the world.
        
        """
        self.world = None