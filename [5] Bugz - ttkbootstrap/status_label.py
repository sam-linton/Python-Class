#
# StatusLabel
#
import ttkbootstrap as ttk
from app_state import AppState


class StatusLabel(ttk.Label):
    '''
    Status Label (shows run state of the application)
    
    '''
    
    def __init__(self, parent) -> None:
        '''
        Initialize
        
        '''
        super().__init__(parent, text = 'Status:')
        self.pack(side = 'top', expand = False, fill = 'x', padx = 2, pady = 5)

    def set_app_state(self, app_state_str: str) -> None:
        '''
        Set application state
        
        '''
        self['text'] = f'Status: {app_state_str}'