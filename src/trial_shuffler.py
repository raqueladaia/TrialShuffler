from m5stack import *
# from m5stack_ui import M5Screen, M5Label, M5Dropdown, M5Switch
from m5stack_ui import *
from uiflow import *

from menu_screen import MenuScreen


def default_protocol():
    protocol = {
        'n_animals': 4,
        'n_stims': 30,
        'paw_left': True,
        'paw_right': True,
    }
    return protocol


class ProtocolScreen(MenuScreen):
    def __init__(self, screen, actions=['', '', 'next']):
        super().__init__(screen, actions)

        self.ui_stim_label = None
        self.ui_stim_count = None
        self.ui_paw_left_lable = None
        self.ui_paw_left_switch = None
        self.ui_paw_right_lable = None
        self.ui_paw_right_switch = None
        self.protocol = default_protocol()
        self.max_stims = 100
        self._align_x_left = 10
        self._align_x_right = 180
        self._y_spacing = 40
        self._color_bg = 0x333333
        self._color_font = 0xFFFFFF
        self._font = FONT_MONT_20

    def set_protocol(self, protocol):
        self.protocol = protocol

    def build_ui(self):
        screen.clean_screen()
        screen.set_screen_bg_color(self._color_bg)
        y = 20

        # UI: number of stimulations
        self.ui_stim_label = M5Label(
            'stimulations',
            x=self._align_x_left,
            y=y,
            color=self._color_font,
            font=self._font,
        )

        self.ui_stim_count = M5Dropdown(
            x=self._align_x_right,
            y=y,
        )
        # set_options(list...) seems not to be working correctly
        for i in range(self.max_stims):
            self.ui_stim_count.add_option(str(i), i)
        stim_index = self.protocol['n_stims']
        self.ui_stim_count.set_sel_index(stim_index)

        # UI: Paw toggles
        y += self._y_spacing
        self.ui_paw_left_lable = M5Label(
            text='left paw',
            x=self._align_x_left,
            y=y,
            color=self._color_font,
            font=self._font,
        )
        self.ui_paw_left_switch = M5Switch(
            x=self._align_x_right,
            y=y,
        )
        if self.protocol['paw_left']:
            self.ui_paw_left_switch.set_on()
        else:
            self.ui_paw_left_switch.set_off()

        y += self._y_spacing
        self.ui_paw_right_lable = M5Label(
            text='right paw',
            x=self._align_x_left,
            y=y,
            color=self._color_font,
            font=self._font,
        )
        self.ui_paw_right_switch = M5Switch(
            x=self._align_x_right,
            y=y,
        )
        if self.protocol['paw_right']:
            self.ui_paw_right_switch.set_on()
        else:
            self.ui_paw_right_switch.set_off()

    def build_response(self):
        index = self.ui_stim_count.get_sel_index()
        self.protocol['n_stims'] = index
        self.protocol['paw_left'] = self.ui_paw_left_switch.get_state()
        self.protocol['paw_right'] = self.ui_paw_right_switch.get_state()
        return self.protocol


class DebugScreen(MenuScreen):
    def __init__(self, screen, actions=['prev', '', 'next']):
        super().__init__(screen, actions)

        self.ui_stim_label = None
        self.ui_left_paw_label = None
        self.ui_right_paw_label = None
        self.protocol = default_protocol()

    def set_protocol(self, protocol):
        self.protocol = protocol

    def build_ui(self):
        screen.clean_screen()
        screen.set_screen_bg_color(0xAA33AA)
        self.ui_stim_label = M5Label('# of stimulations:' + str(self.protocol['n_stims']), x=10, y=20)
        self.ui_left_paw_label = M5Label('left paw:' + str(self.protocol['paw_left']), x=10, y=60)
        self.ui_right_paw_label = M5Label('right paw:' + str(self.protocol['paw_right']), x=10, y=100)
    
    def build_response(self):
        return self.protocol



screen = M5Screen()
proto_screen = ProtocolScreen(screen, actions=['', 'stim', 'debug'])
# proto_screen.set_nav_color(0xFF00FF)
dbg_screen = DebugScreen(screen, actions=['stim', '', ''])

protocol = default_protocol()

action = 'stim'
while action:
    wait_ms(5)
    if action == 'stim':
        dbg_screen.set_protocol(protocol)
        action, protocol = proto_screen.activate()
    elif action == 'debug':
        dbg_screen.set_protocol(protocol)
        action, protocol = dbg_screen.activate()
    else:
        break

screen.clean_screen()
screen.set_screen_bg_color(0xFF3300)
ui_stim_label = M5Label('# STIMS:' + action + ' -- ' + str(protocol['n_stims']), x=10, y=30)

