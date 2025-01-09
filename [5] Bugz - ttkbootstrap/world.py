#
# World
#
import ttkbootstrap as ttk
import random
import math
from enum import Enum
from app_state import AppState
from actor import Actor, NORTH, EAST, SOUTH, WEST
from bug import Bug
from flower import Flower
from rock import Rock


class World(ttk.Canvas):
    '''
    Holds all the actors.
    
    '''
    
    def __init__(self, parent, app_state: AppState) -> None:
        '''
        Initialize
        
        '''
        super().__init__(parent, bg = '#9999ff')
        
        self.bind('<Configure>', lambda event: self.__resize(event))
        self.imax: int = 20 # cells
        self.jmax: int = 20
        self.xmax: float = 0
        self.ymax: float = 0
        self.app_state = app_state
        self.replace_ok: bool = False
        self.actors_dict: dict = {}
        
        self.add_actors()
        
    def add_actors(self) -> None:
        '''
        Override this in a derived class
        
        '''
        pass
        
    def compute_actor_size(self) -> int:
        '''
        Figure out the size available for an actor based on the world size
        
        '''
        return math.floor((min(self.xmax, self.ymax) - 5) / self.imax)
    
    def reset(self) -> None:
        '''
        Reset the world state to the original configuration.
        
        '''
        self.remove_all_actors()
        self.add_actors()
        size = self.compute_actor_size()
        for actor in self.actors_dict.values():
            actor.resize(size)
        self.draw()
        
    def __resize(self, event) -> None:
        '''
        Resize world to fit in the window.
        
        '''
        mindim = min(event.width, event.height) - 5
        self.xmax = mindim
        self.ymax = mindim
        size = self.compute_actor_size()
        for actor in self.actors_dict.values():
            actor.resize(size)
        self.draw()
    
    def draw(self) -> None:
        '''
        Draw the entire world and its actors
        
        '''
        self.delete('all')
        self.__draw_grid()
        for actor in self.actors_dict.values():
            actor.draw(self)
    
    def __draw_grid(self) -> None:
        '''
        Draw the grid in the world.
        
        '''
        dy = self.ymax / self.jmax
        for j in range(self.jmax + 1):
            y = j * dy
            self.create_line(0, y, self.xmax, y)
            
        dx = self.xmax / self.imax
        for i in range(self.imax + 1):
            x = i * dx
            self.create_line(x, 0, x, self.ymax)
            
    def get_x(self, i: int) -> float:
        '''
        Get the x value corresponding to the (i, j) coordinates.
        
        '''
        dx: float = self.xmax / self.imax
        return i * dx
    
    def get_y(self, j: int) -> float:
        '''
        Get the y value corresponding to the (i, j) coordinates.
        
        '''
        dy: float = self.ymax / self.jmax
        return j * dy
    
    def get_imax(self) -> int:
        '''
        Return max i index for the cells
        
        '''
        return self.imax
    
    def get_jmax(self) -> int:
        '''
        Return max j index for the cells
        
        '''
        return self.jmax
    
    def get_next_coords(self, coords: tuple[int, int], direction: int) -> tuple[int, int]:
        '''
        Return the coordinates in the specified direction
        relative to the supplied coordinates
        '''
        i, j = coords
        if direction == NORTH:
            j-=1
        elif direction == SOUTH:
            j+=1
        elif direction == WEST:
            i-=1
        elif direction == EAST:
            i+=1
        else:
            error('Bad direction value in get_next_coords')
        
        return (i, j)
    
    def add(self, actor: Actor, i: int, j: int, direction: int) -> bool:
        '''
        Add an actor to this world at the provided coordinates.
        
        '''
        if not self.__in_bounds(i, j):
            self.error(f'Attempt to add actor at invalid location: ({i},{j})')
            return False
        
        if not self.replace_ok and not self.is_available(i,j):
            self.error(f'Attempt to add actor to occupied location: ({i},{j}')
            return False
        
        self.actors_dict[(i, j)] = actor
        actor.world = self
        actor.i = i
        actor.j = j
        if not direction == actor.direction:
            actor.set_direction(direction)
        return True
    
    def remove(self, actor: Actor) -> bool:
        '''
        Remove an actor from the world.
        
        '''
        if actor.world is None:
            self.error(f'Unsuccessful attempt to remove actor at ({actor.i},{actor.j}) from world.')
            return False
        
        actor.world = None
        del self.actors_dict[(actor.i, actor.j)]
        return True
    
    def remove_all_actors(self) -> None:
        '''
        Remove all the actors from the world.
        
        '''
        self.actors_dict = {}
         
    def is_available(self, i: int, j: int) -> bool:
        '''
        Check whether the space at the provided coordinates is available to be moved into.
        
        '''
        return self.__in_bounds(i, j) and (i, j) not in self.actors_dict
     
    def get_actor(self, i: int, j: int) -> Actor | None:
        '''
        Get the actor at the provided coordinates (or None)
        
        '''
        if not self.__in_bounds(i, j): return None
        if (i, j) not in self.actors_dict: return None
        return self.actors_dict[(i,j)]
    
    def get_all_actors(self) -> list[Actor]:
        '''
        Get all the actors
        
        '''
        return [actor for actor in self.actors_dict.values()]

    def move_actor_to(self, actor: Actor, inew: int, jnew: int) -> bool:
        '''
        Move specified actor to the specified coordinates.
        
        '''
        if not self.remove(actor):
            return False
        return self.add(actor, inew, jnew, actor.direction)
        
    def act(self) -> None:
        '''
        Act for one timestep.
        
        '''
        for actor in self.get_all_actors():
            actor.act()                   
                    
    def __in_bounds(self, i: int, j: int) -> bool:
        '''
        True if the provided coordinates is in bounds in the world.
        
        '''
        return 0 <= i < self.imax and 0 <= j < self.jmax
    
    def error(self, message: str) -> None:
        '''
        Set error state and message.
        
        '''
        print('Error: ' + message)
        self.app_state.set(AppState.ERROR)
    
    def add_multiple_actors(self, entries: list) -> None:
        '''
        Add multiple actors to the world.
        
        '''
        for entry in entries:
            print(entry)
            actor, i, j, direction = entry
            self.add(actor, i, j, direction)
            print(f'number of actors = {len(self.actors_dict)}')
            
    def add_random_actors(self, num_rocks:int = 25, num_flowers:int = 25, num_bugs:int = 2) -> None:
        '''
        Randomly add in actors to the world.
        
        '''
        max_possible = self.imax * self.jmax
        num_rocks = min(num_rocks, max_possible)
        num_flowers = min(num_flowers, max_possible)
        num_bugs = min(num_bugs, max_possible)
        
        # TODO: create list of empty cells, and remove them as you add
        # Then get rid of replace_ok
        self.replace_ok = True # Temporarily ok to put Actor onto an occupied space
        
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

    def run(self) -> None:
        '''
        Start the world running.
        
        '''
        if (self.app_state.is_state(AppState.RUNNING)):
            self.run_one_step()
            self.after(500, self.run)
            
    def run_one_step(self) -> None:
        '''
        Advance the world one timestep.
        
        '''
        self.act()
        self.draw()