from m5stack import *
from m5stack_ui import *
from uiflow import *


class MenuScreen:
    ''' Base class for screen based menus.

        The actual UI is built by implementing 'build_ui()'. That
        method is autimatically called when the menu screen is
        activated.
        
        Navigation is supported via the M5Stack buttons A, B, C.
        To enable those buttons, define the list of 'actions' in the
        constructor. Empty strings are treated as no action defined.

        The action string that is returned when the button is pressed
        E.g. in the above example, when the user clicks the left button,
        'activate()' would return "back".

        To return more information from the screen (e.g. entered values),
        implement the 'build_response()' and return the desired object.
        This function is autimatically called after the user presses a
        navigation button and returns the value.
    
        USAGE EXAMPLE:
        ##########################################################
        class MyMenu(MenuScreen):
            ...

            def build_ui(self):
                # create the ui here using M5Stack ui element
                ...

            def build_response(self):
                # called upon exiting the screen
                # return any values here, e.g. entered in te UI

        screen = M5Screen()
        # define a screen with left and center buttons enables
        my_menu = MyMenu(screen, actions=['back', 'accept', ''])
        action, response = my_menu.activate()

    '''
    def __init__(self, screen, actions=['', '', 'next']):
        self.screen = screen
        self.actions = actions
        self.nav_labels = [None, None, None]
        self.nav_color = 0xFFFF00

    def set_nav_color(self, color):
        self.nav_color = color

    # @abstractmethod
    def build_ui(self):
        pass

    # @abstractmethod
    def build_response(self):
        pass

    def _build_nav_ui(self):
        for label in self.nav_labels:
            if label:
                label.delete()

        nav_icons = ('<<', 'O', '>>')
        for i, action, in enumerate(self.actions):
            if action:
                x = 47 + 106 * i
                y = 220
                self.nav_labels[i] = M5Label(
                    nav_icons[i],
                    x=x, y=y,
                    color=self.nav_color)

    def activate(self):
        self.build_ui()
        self._build_nav_ui()

        next_action = -1
        while next_action < 0:
            wait_ms(5)
            if self.actions[0] and btnA.isPressed():
                next_action = 0
            if self.actions[1] and btnB.isPressed():
                next_action = 1
            if self.actions[2] and btnC.isPressed():
                next_action = 2

        while btnA.isPressed() or btnB.isPressed() or btnC.isPressed():
            wait_ms(5)

        return self.actions[next_action], self.build_response()
