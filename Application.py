from Window import *
from ProgramLogic import *

class Application:
    def __init__(self, title: str, dim_width: int, dim_height: int):
        """
        @brief    Application class for communicating between Events, program logic, and the
                  renderer.
        @param title    The title to use on the titlebar of the window.
        @param dim_width    The width of the window to display.
        @param dim_height    The height of the window to display.
        """
        self.title = title
        self.dimensions = (dim_width, dim_height)
        self.wd = Window(title, (200, 200, 200), self.dimensions[0], self.dimensions[1])
        self.pl = ProgramLogic(dim_width, dim_height, (0, 0))
        self.isRunning = self.wd.isRunning
        self.delay = 0.010 # seconds
        self.game_tick = 0
        self.window_tick = 0
    
    def tick(self):
        """
        @brief    Executes actions on a gameloop. This function itself does not loop, but is called
                  outside of the class.
            ___________________________________________
           | Function calls                            |
           | * process_events()                        |
           | * ProgramLogic.tick()                     |
           | * Window.update(ProgramLogic.sprite_list) |
           |___________________________________________|
        # TODO: Maybe remove this box
        """
        
        self.game_tick += 1
        self.window_tick += 1
        if self.game_tick == 2:
            self.process_events()
            self.pl.tick(self.game_tick * self.delay * 20)
            self.game_tick = 0
        if not self.isRunning: return
        if self.window_tick == 1:
            self.wd.update(self.pl.sprite_list)
            self.window_tick = 0

    def process_events(self):
        """
        @brief    Pings events like system calls and user input, and executes actions depending
                  on the type.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass

    def quit(self):
        """
        @brief    Ends the Window process and cleans up upon exit.
        """
        self.wd.quit()
        self.isRunning = False
