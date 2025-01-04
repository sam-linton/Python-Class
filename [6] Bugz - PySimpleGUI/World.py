#
# World
#
import PySimpleGUI as sg
from Actor import Actor, NORTH, EAST, SOUTH, WEST
from Flower import Flower
from Rock import Rock
from Bug import Bug
from enum import Enum
import random

# World state
class State(Enum):
    STOPPED = 1
    RUNNING = 2
    STEPPING = 3
    ERROR = 4
    
# World state names
state_names = {State.STOPPED: 'Stopped',
               State.RUNNING: 'Running',
               State.STEPPING: 'Stepping',
               State.ERROR: 'Error'}

class World:
    """
    World includes all the actors
    
    """
    
    def __init__(self):
        """
        Intitialize
        
        """
        self.imax: int = 20
        self.jmax: int = 20
        self.xmin: float = 0.0
        self.xmax: float = 400.0
        self.ymin: float = 0.0
        self.ymax: float = 400.0
        self.state: State = State.STOPPED
        self.replace_ok: bool = False
        self.actors_dict: dict = {}
        
        
    def get_state_name(self)-> str:
        """
        Get the world's state
        
        """
        return state_names[self.state]
        
        
    def populate(self, num_rocks:int = 25, num_flowers:int = 25, num_bugs:int = 2)-> None:
        """
        Use to add rocks, flowers, and bugs into a world.
        
        """
        max_possible = self.imax * self.jmax
        num_rocks = min(num_rocks, max_possible)
        num_flowers = min(num_flowers, max_possible)
        num_bugs = min(num_bugs, max_possible)
        
        self.replace_ok = True
        
        count = 0
        while (count < num_rocks):
            if self.add(Rock(), random.randint(0, self.imax-1), random.randint(0, self.jmax-1), NORTH):
                count+=1
            
        count = 0
        while (count < num_flowers):
            if self.add(Flower(), random.randint(0, self.imax-1), random.randint(0, self.jmax-1), NORTH):
                count+=1
            
        count = 0
        while (count < num_bugs):
            direction = random.choice((NORTH, EAST, SOUTH, WEST))
            if self.add(Bug(), random.randint(0, self.imax), random.randint(0, self.jmax), direction):
                count+=1
                
        self.replace_ok = False
        
        
    def get_sg_canvas(self)-> sg.Canvas:
        """
        Get the canvas
        
        """
        xsize = self.xmax - self.xmin
        ysize = self.ymax - self.ymin
        return sg.Canvas(size=(xsize, ysize), background_color='white', key='-CANVAS-')
    
    
    def finalize(self, window: sg.Window)-> None:
        """
        Needed to finalize the World.
        
        """
        self.canvas = window['-CANVAS-'].TKCanvas
            
            
    def get_x(self, i: int)-> float:
        """
        Get the x value corresponding to the provided i index. For Interal use only.
        
        """
        dx: float = (self.xmax - self.xmin) / self.imax
        return self.xmin + i * dx
    
    
    def get_y(self, j: int)-> float:
        """
        Get the x value corresponding to the provided i index. For Interal use only.
        
        """
        dy: float = (self.ymax - self.ymin) / self.jmax
        return self.ymin + j * dy
    
          
    def draw_grid(self)-> None:
        """
        Draw the grid
        
        """
        self.canvas.create_rectangle(self.xmin, self.xmax, self.ymin, self.ymax)
        
        dx: float = (self.xmax - self.xmin) / self.imax
        dy: float = (self.ymax - self.ymin) / self.jmax
        
        for i in range(self.imax+1):
            x: float = self.xmin + i * dx
            self.canvas.create_line(x, self.ymin, x, self.ymax)
        
        for j in range(self.jmax+1):
            y: float = self.ymin + j * dy
            self.canvas.create_line(self.xmin, y, self.xmax, y)
            
    
    def draw(self)-> None:
        """
        Draw everything: the grid and all the actors.
        
        """
        self.canvas.delete("all")
        self.draw_grid()
        for actor in self.actors_dict.values():
            actor.draw(self.canvas)
                    
                    
    def in_bounds(self, i: int, j: int)-> bool:
        """
        return true if the indices are inbounds
        
        """
        return 0 <= i < self.imax and 0 <= j < self.jmax
        

    def error(self, message: str)-> None:
        """
        Call when an error occurs
        
        """
        print('Error: ' + message)
        self.state = State.ERROR
    
    
    def add(self, actor: Actor, i: int, j: int, direction: int)-> bool:
        """
        Add an actor to the world at the position and with the direction provided.
        
        """
        if not self.in_bounds(i, j):
            self.error(f'Attempt to add actor at invalid location: ({i},{j})')
            return False
        if not self.replace_ok and not self.is_available(i,j):
            self.error(f'Attempt to add actor to occupied location: ({i},{j}')
            return False
        self.actors_dict[(i, j)] = actor
        actor.world = self
        actor.i = i
        actor.j = j
        actor.set_direction(direction)
        return True
        
        
    def remove(self, actor: Actor)-> bool:
        """
        Remove the actor from the world. Note: this is for internal use only!
        Use actor.remove_self_from_world instead.
        
        """
        if actor.world is None:
            self.error(f'Unsuccessful attempt to remove actor at ({actor.i},{actor.j}) from world.')
            return False
        actor.world = None
        del self.actors_dict[(actor.i, actor.j)]
        return True
         
         
    def is_available(self, i: int, j: int)-> bool:
        """
        Returns true if the cell at (i, j) is inbounds and unoccuppied
        
        """
        return self.in_bounds(i, j) and (i, j) not in self.actors_dict
     
     
    def get_actor(self, i: int, j: int)-> Actor | None:
        """
        Get the actor at (i, j)
        
        """
        if not self.in_bounds(i, j): return None
        if (i, j) not in self.actors_dict: return None
        return self.actors_dict[(i,j)]
    
    
    def get_all_actors(self)-> list[Actor]:
        """
        Return a list of all the actors in the world.
        
        """
        return [actor for actor in self.actors_dict.values()]


    def move_actor_to(self, actor: Actor, inew: int, jnew: int)-> bool:
        """
        Move specified actor to the new location
        
        """
        if not self.remove(actor):
            return False
        return self.add(actor, inew, jnew, actor.direction)

        
    def act(self)-> None:
        """
        Perform single timestep
        
        """
        if self.state in (State.STOPPED, State.ERROR):
            return

        for actor in self.get_all_actors():
            actor.act()
                    
        if self.state == State.STEPPING:
            self.state = State.STOPPED 