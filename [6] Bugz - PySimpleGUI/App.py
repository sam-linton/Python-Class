#
# App
#
import PySimpleGUI as sg
from World import World, State


class App:
    """
    Main app for the Bugz Application.
    
    """
    
    def __init__(self):
        """
        Initialize
        
        """
        sg.theme('DarkAmber')
        
        self.world: World = World()
        self.world.populate()
        
        # Instructions: Add in your Bug here

        self.create_window()
        self.world.finalize(self.window)
        
    def create_window(self)-> None:
        """
        Create the main application window
        
        """
        layout: list = [
            [
                sg.Column([[self.world.get_sg_canvas()]]),
                sg.Column([
                    [sg.Text('Status', key='-STATUS-')],
                    [sg.Button('Start', key='-START-'),
                        sg.Button('Step', key='-STEP-'),
                        sg.Button('Stop', key='-STOP-'),
                        sg.VPush()]
                    ], key='-CONTROLS-')
             ]
        ]
        self.window: sg.Window = sg.Window('Bugz', layout, finalize=True)
        
    def run(self)-> None:
        """
        Start run
        
        """
        while True:
            event, values = self.window.read(timeout = 300)        
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            
            elif event == '-START-':
                print('start')
                self.world.state = State.RUNNING
            elif event == '-STOP-':
                self.world.state = State.STOPPED
            elif event == '-STEP-':
                self.world.state = State.STEPPING
                
            self.window['-STATUS-'].update(f'Status: {self.world.get_state_name()}')

            self.world.act()
            self.world.draw()
            
        self.window.close()

        
    def draw(self)-> None:
        """
        Draw all
        
        """
        self.world.draw()
