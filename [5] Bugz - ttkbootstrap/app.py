#
# App
#
import ttkbootstrap as ttk
from app_state import AppState
from control_panel import ControlPanel
from bug_world import BugWorld


class App(ttk.Window):
    '''
    The main window for the application
    
    '''
    def __init__(self) -> None:
        '''
        Initialize
        
        '''
        super().__init__(themename = 'darkly')
        self.geometry('800x600')
        self.title('Bugz!')
        
        app_state: AppState = AppState()
        self.world: BugWorld = BugWorld(self, app_state)
        self.control_panel: ControlPanel = ControlPanel(self, app_state, self.world);
        self.world.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.control_panel.pack(side = 'left', fill = 'both')
        
        self.mainloop()