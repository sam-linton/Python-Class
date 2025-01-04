#
# ControlPanel
#
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from app_state import AppState
from bug_world import BugWorld
from status_label import StatusLabel


class ControlPanel(ttk.Frame):
    '''
    ControlPanel - holds buttons to control run
    
    '''
    
    def __init__(self, parent, app_state: AppState, world: BugWorld) -> None:
        '''
        Initialize
        
        '''
        super().__init__(parent, bootstyle='info')
        
        self.app_state = app_state
        self.world = world
        
        # Status Label
        self.status_label = StatusLabel(self)
        self.set_app_state(app_state.get())
        
        # Toolbar
        tool_bar = ttk.Frame(self, bootstyle = 'secondary')
        tool_bar.pack(side = 'top', expand = False, fill = 'x', padx = 2, pady = 5, ipadx = 2, ipady = 2)
        
         # Single Step Button
        image_original: Image = Image.open('images/step_image.png').resize((50, 50))
        image_tk: ImageTk = ImageTk.PhotoImage(image_original)
        step_button = ttk.Button(tool_bar, text = 'Step', image = image_tk, compound = 'right', command = self.step)
        step_button.pack(side = 'left', padx = 2)
        
        # Start Button
        start_button = ttk.Button(tool_bar, text = 'Start', command = self.start)
        start_button.pack(side = 'left', padx = 2)

        # Stop Button
        stop_button = ttk.Button(tool_bar, text = 'Stop', command = self.stop)
        stop_button.pack(side = 'left', padx = 2)
        
        # Reset Button
        reset_button = ttk.Button(tool_bar, text = 'Reset', command = self.reset)
        reset_button.pack(side = 'left', padx = 2)
        
    def step(self) -> None:
        '''
        Run one timestep.
        
        '''
        print('step')
        self.set_app_state(AppState.STEPPING)
        self.world.run_one_step()
        self.set_app_state(AppState.STOPPED)
    
    def start(self) -> None:
        '''
        Start the run.
        
        '''
        print('start')
        self.set_app_state(AppState.RUNNING)
        self.world.run()
    
    def stop(self) -> None:
        '''
        Stop the run.
        
        '''
        print('stop')
        self.set_app_state(AppState.STOPPED)
        
    def reset(self) -> None:
        '''
        Reset the world to the original configuration.
        '''
        print('reset')
        self.set_app_state(AppState.STOPPED)
        self.world.reset()
        
    def set_app_state(self, app_state_str: str) -> None:
        '''
        Set the application state
        
        '''
        self.app_state.set(app_state_str)
        self.status_label.set_app_state(app_state_str)
