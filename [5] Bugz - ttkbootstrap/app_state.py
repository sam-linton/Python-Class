#
# AppState
#
#
# import tkinter as tk
import ttkbootstrap as ttk

class AppState:
    '''
    Application State
    
    '''
    STOPPED = 'Stopped'
    RUNNING = 'Running'
    STEPPING = 'Stepping'
    ERROR = 'Error'
    
    def __init__(self) -> None:
        '''
        Initialize
        
        '''
        self.__state = AppState.STOPPED
        #self.state_text = ttk.StringVar(self.__state)
        #self.state_text = ttk.StringVar('STOPPED');
        #self.state_text = 'hi'
        
    def set(self, state: str) -> None:
        '''
        Set the state
        
        '''
        self.__state = state
        #self.state_text.set(self.__state)
        
    def is_state(self, state: str) -> bool:
        '''
        Check to see if the state matches the provided value
        
        '''
        return self.__state == state
    
    def get(self) -> str:
        '''
        Get the state
        
        '''
        return self.__state
        
        
    
        